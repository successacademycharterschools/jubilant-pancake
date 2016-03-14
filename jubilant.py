from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
import json

PORT = 5555


def levenshtein(string1=None, string2=None):
    '''algorithm taken from wikipedia article here:
    https://en.wikipedia.org/wiki/Levenshtein_distance
    iterative version with two matrix rows'''

    # handle cases where strings are the same or one is empty
    if string1 == string2:
        return 0
    elif len(string1) == 0:
        return len(string2)
    elif len(string2) == 0:
        return len(string1)

    # create vectors
    v0 = [None] * (len(string2) + 1)
    v1 = [None] * (len(string2) + 1)
    for i in range(len(v0)):
        v0[i] = i
    for i in range(len(string1)):
        v1[0] = i + 1
        #calculate cost
        for j in range(len(string2)):
            cost = 0 if string1[i] == string2[j] else 1
            v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
        for j in range(len(v0)):
            v0[j] = v1[j]

    return v1[len(string2)]


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
        print(self.data_string)

        levenshtein_args = json.loads(self.data_string.decode("utf-8"))
        print(levenshtein_args)

        self.send_response(200)
        self.send_header("Content-type:", "text/html")

        # self.end_headers()  ##Seriously. Find out why this doesn't work.
        self.wfile.write(bytes("\n", 'utf-8'))

        dist = {"dist": levenshtein(levenshtein_args['string1'],
                           levenshtein_args['string2'])}
        print(dist)
        data = json.dumps(dist)
        self.wfile.write(bytes(data, 'utf-8'))
        return


if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), MyRequestHandler)
    print("serving on port: {}".format(PORT))
    server.serve_forever()
