#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse
from tornado.web import (
    Application,
    RequestHandler,
    )
from tornado.websocket import WebSocketHandler
from tornado.ioloop import IOLoop
from sandstorm.handlers import YAStaticFileHandler
from sandstorm.config import Configurator


class MainHandler(RequestHandler):
    def get(self):
        self.render('index.html')


class RTDisplayHandler(WebSocketHandler):
    pass


def includeme(config, prefix):
    pass


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', default='localhost')
    parser.add_argument('--port', default=8080, type=int)
    args = parser.parse_args(argv)

    config = Configurator()
    config.include('.')

    app = Application([
        (r'/', YAStaticFileHandler()),
    ])
    app.listen(args.port)
    loop = IOLoop.instance()
    loop.start()

if __name__ == '__main__':
    sys.exit(main())
