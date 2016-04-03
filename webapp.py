"""
Webserver and main entry point.
Requires python 3.5 with tornado.
    python webapp.py --env=[dev|prd] --configdir=[Folder with config.json]
Configuration:
    Requires config.[ENV].json file in [CONFIGDIR] to specify, in particular:
        host address and ports to listen on
        ssl key and certificate location if terminated in-app
"""

import json
import datetime as DT
from tornado import ioloop, options, web, gen

from py import config  # parses config.json on load
from py import calcs


class genindex(web.RequestHandler):
    """
    Main entry point: index.html
    """
    def get(self, *ar, **kw):
        self.render(
            'index.html',
            current_user=self.current_user,
            )


class calculate(web.RequestHandler):
    """
    Calculates the edit distance between two strings.
    """
    def post(self, *ar, **kw):
        """
        Taylored for Angular's $http.post: json in the body of the request
        """
        req = json.loads(self.request.body.decode('utf-8'))
        distance = calcs.levenshtein(req.get('v1', ''), req.get('v2', ''))
        self.write(dict(
            distance=distance,
        ))


if __name__ == '__main__':
    print(
        '>> starting webserver',
        DT.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )
    # app configuration, mostly from py.config
    appcon = dict(
        static_path=options.options.static_path,
        template_path=options.options.template_path,
        cookie_secret=options.options.secret,
        login_url='/login',
        debug=options.options.debug,
        )
    # app routes
    genapp = web.Application(
        [
            (r"/calculate(.*)", calculate),
            (r"/(.*)", genindex),
        ],
        **appcon)
    genapp.listen(options.options.genport, address=options.options.host)
    ioloop.IOLoop.current().start()
