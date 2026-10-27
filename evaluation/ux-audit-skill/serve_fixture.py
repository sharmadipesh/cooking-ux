"""Loopback-only synthetic audit server; never creates accounts or stores payloads."""
import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import time

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.split('?')[0] != '/registration.html':
            self.send_error(404)
            return
        body=(Path(__file__).parent/'fixtures/registration.html').read_bytes()
        self.send_response(200)
        self.send_header('Content-Type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        if self.path != '/api/request-access':
            self.send_error(404)
            return
        self.rfile.read(int(self.headers.get('Content-Length','0')))
        time.sleep(0.2)
        self.send_response(422)
        self.send_header('Content-Type','application/json')
        self.end_headers()
        self.wfile.write(b'{"message":"Use a different email address."}')

    def log_message(self,*args):
        pass

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port',type=int,default=0)
    args=parser.parse_args()
    server=ThreadingHTTPServer(('127.0.0.1',args.port),Handler)
    print('http://127.0.0.1:'+str(server.server_port)+'/registration.html',flush=True)
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()
