from http.server import BaseHTTPRequestHandler, HTTPServer
import subprocess

class ShutdownHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/stop':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            # running the shutdown script
            subprocess.call(['sh', '/usr/share/nginx/html/sd.sh'])

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 9999), ShutdownHandler).serve_forever()
