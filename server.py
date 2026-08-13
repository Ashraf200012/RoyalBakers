import http.server
import os

class MyCGIHandler(http.server.CGIHTTPRequestHandler):
    # Allow CGI scripts to be run from the root directory instead of just cgi-bin
    cgi_directories = ['/']

PORT = int(os.environ.get("PORT", 8080))
print(f"Starting CGI server on port {PORT}...")
http.server.test(HandlerClass=MyCGIHandler, port=PORT)
