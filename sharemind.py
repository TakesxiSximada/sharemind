#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse
from tornado.web import (
    Application,
    RequestHandler,
    StaticFileHandler,
    )
from tornado.websocket import (
    WebSocketHandler,
    )
from tornado.ioloop import IOLoop
# from sandstorm.handlers import YAStaticFileHandler


class MainHandler(RequestHandler):
    def get(self):
        self.render('index.html')


class RTDisplayHandler(WebSocketHandler):
    pass


def includeme(config, prefix):
    pass


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', default=8080, type=int)
    args = parser.parse_args(argv)

    app = Application([
        (r'/', StaticFileHandler, {'path': 'www'}),
    ], **{'debug': True, 'route_prefix': ''})
    app.listen(args.port)
    loop = IOLoop.instance()
    loop.start()

if __name__ == '__main__':
    sys.exit(main())
