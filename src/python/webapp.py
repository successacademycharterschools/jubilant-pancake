#!/usr/bin/env python2.7

import ConfigParser


from webob import Request
from webob import Response
from webob import dec


class StringComparitorApp(object):

    def __init__(self, config):
        self.dispatch = {
            "GET": self.page,
            "POST": self.compare,
        }
        with open(config.get("web", "page_filename"), "r") as pf:
            self.page_content = pf.read()

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
        response.body = self.page_content
        return response


def run_server(app, config):
    from wsgiref.simple_server import make_server
    host = config.get("site", "host")
    port = config.get("site", "port")
    httpd = make_server(host, port, app)
    print 'Serving on http://localhost:5678'
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print '^C'


def main():
    config = ConfigParser.SafeConfigParser()
    with open("defaults.cfg", "r") as config_defaults:
        config.readfp(config_defaults)

    app = StringComparitorApp(config)

    run_server(app, config)


if __name__ == "__main__":
    main()
