#!/usr/bin/env python2.7

from webob import Request
from webob import Response
from webob import dec
from webob import exc


class StringComparitorApp(object):

    def __init__(self):
        self.dispatch = {
            "GET": self.page,
            "POST": self.compare,
        }

    @dec.wsgify
    def __call__(self, req):
        try:
            return self.dispatch[req.method](req)
        except KeyError:
            fail_default = Response()
            fail_default.status_int = 500
            return fail_default

    @dec.wsgify
    def compare(self, req):
        response = Response()
        return response

    @dec.wsgify
    def page(self, req):
        response = Response()
        return response


def main():
    app = StringComparitorApp()
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', '5678', app)
    print 'Serving on http://localhost:5678'
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print '^C'


if __name__ == "__main__":
    main()
