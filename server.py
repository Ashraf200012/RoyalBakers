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

PORT = int(os.environ.get("PORT", 8080))
print(f"Starting CGI server on port {PORT}...")
http.server.test(HandlerClass=MyCGIHandler, port=PORT)
