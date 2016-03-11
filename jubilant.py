from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import json

PORT = 5555

# dist = {"dist": "2"}

def levenshtein(string1=None, string2=None):
    dist = {"dist": "2"}
    return dist


class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.path = "index.html"
            self.send_response(200)
            self.send_header("Content-type:", "text/html")

            # self.end_headers()  ##WTF?
            self.wfile.write(bytes("\n", 'utf-8'))
            f = open(self.path)
            self.wfile.write(bytes(f.read(), 'utf-8'))
            f.close()
        return

    def do_POST(self):
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        # print(self.data_string)

        levenshtein_args = json.loads(self.data_string.decode("utf-8"))
        print(levenshtein_args)

        self.send_response(200)
        self.send_header("Content-type:", "text/html")

        # self.end_headers()  ##Seriously. Find out why this doesn't work.
        self.wfile.write(bytes("\n", 'utf-8'))

        dist = levenshtein(levenshtein_args['string1'],
                           levenshtein_args['string2'])
        data = json.dumps(dist)
        self.wfile.write(bytes(data, 'utf-8'))
        return


if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), MyRequestHandler)
    print("serving on port: {}".format(PORT))
    server.serve_forever()
