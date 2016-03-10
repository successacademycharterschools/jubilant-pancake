from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import json

PORT = 5555

dist = {"dist": "2"}

class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.path = "index.html"
            self.send_response(200)
            self.send_header("Content-type:", "text/html")
            self.wfile.write(bytes("\n", 'utf-8'))
            f = open(self.path)
            self.wfile.write(bytes(f.read(), 'utf-8'))
            f.close()


        if self.path == "/measure":
            #send response code:
            self.send_response(200)
            #send headers:
            self.send_header("Content-type:", "text/html")
            # self.end_headers()
            # send a blank line to end headers:
            self.wfile.write(bytes("\n", 'utf-8'))

            #send response:
            self.wfile.write(bytes(json.dumps(dist), 'utf-8'))
        return


if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), MyRequestHandler)
    print("serving on port: {}".format(PORT))
    server.serve_forever()
