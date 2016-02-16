#!/usr/bin/env python2.7

"""
This is the sample coding challenge for Success Academy.

It's a simple Python app that runs a very small framework
constructed on top of the WebOb libraries.
"""

import ConfigParser
import json
import os.path

import editdistance

from webob import Response
from webob import dec


class StringComparitorApp(object):

    def __init__(self, config):
        self.dispatch = {
            "GET": self.page,
            "POST": self.compare,
        }
        module_dir = os.path.dirname(os.path.abspath(__file__))
        page_filename = config.get("web", "page_filename")
        page_path = os.path.abspath(os.path.join(module_dir, page_filename))
        with open(page_path, "r") as page:
            self.page_content = page.read()

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
        inputs = json.loads(req.body)
        distance = editdistance.eval(inputs["source"], inputs["target"])
        response = Response()
        response.type = 'application/json'
        response.body = json.dumps({"edit_distance": int(distance)})
        return response

    @dec.wsgify
    def page(self, req):
        """
        This is the response to a GET on the site - return the cached
        webpage.
        """
        response = Response()
        response.body = self.page_content
        return response


def run_server(app, config):
    from wsgiref.simple_server import make_server
    hostname = config.get("site", "hostname")
    port = int(config.get("site", "port"))
    httpd = make_server(hostname, port, app)
    print 'Serving on http://{}:{}'.format(hostname, port)
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
