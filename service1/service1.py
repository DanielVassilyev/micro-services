import requests
import os
import subprocess
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class Service1(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            service1_info = {
                'ip': os.popen('hostname -I').read().strip(),
                'processes': os.popen('ps -ax').read(),
                'disk': os.popen('df -h /').read(),
                'uptime': os.popen('uptime -p').read()
            }
            # getting the data from service2
            service2_info = requests.get('http://service2:8500/data').json()

            combined_info = {
                'service1': service1_info,
                'service2': service2_info
            }

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            # convering and sending
            self.wfile.write(json.dumps(combined_info).encode())
            
if __name__ == '__main__':
    # 0.0.0.0 is used to make it accessible from outside of the container
    HTTPServer(('0.0.0.0', 8199), Service1).serve_forever()