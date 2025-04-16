from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
       def do_GET(self):
           print("Received GET request")
           print("Path:", self.path)
           print("Headers:", self.headers)
           self.send_response(200)
           self.send_header('Content-Type', 'text/html')
           self.end_headers()
           message = f"<html><body><h1>Hello, HTTP World!</h1><p>You requested: {self.path}</p></body></html>"
           self.wfile.write(message.encode('utf-8'))

       def do_POST(self):
           content_length = int(self.headers.get('Content-Length', 0))
           post_data = self.rfile.read(content_length)
           print("Received POST request")
           print("Path:", self.path)
           print("Headers:", self.headers)
           print("Body:", post_data.decode('utf-8'))
           self.send_response(200)
           self.send_header('Content-Type', 'text/plain')
           self.end_headers()
           self.wfile.write(b"POST request received!")

def run(server_class=HTTPServer, handler_class=MyHandler, port=8000):
       server_address = ('', port)
       httpd = server_class(server_address, handler_class)
       print(f"Starting HTTP server on port {port}...")
       httpd.serve_forever()

if __name__ == '__main__':
       run()
   