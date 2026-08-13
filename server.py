import http.server
import os

class MyCGIHandler(http.server.CGIHTTPRequestHandler):
    cgi_directories = ['/']

    def is_cgi(self):
        # Redirect the main website URL to home.py
        if self.path == '/':
            self.path = '/home.py'
            
        # Run the default check to set up the script path
        is_script = super().is_cgi()
        
        # ONLY run it as a CGI script if it is a .py file
        if is_script and self.path.split('?')[0].endswith('.py'):
            return True
            
        # For all other files (css, images, html), serve them normally
        return False

if __name__ == '__main__':
    # Force the server to bind to 0.0.0.0 so Render can see it
    PORT = int(os.environ.get("PORT", 8080))
    server_address = ('0.0.0.0', PORT)
    print(f"Starting CGI server on 0.0.0.0:{PORT}...")
    
    httpd = http.server.HTTPServer(server_address, MyCGIHandler)
    httpd.serve_forever()
