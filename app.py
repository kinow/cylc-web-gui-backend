import logging
import tornado.ioloop
import tornado.web
import sys

from auth import Authenticator

from container import IocContainer


class MainHandler(tornado.web.RequestHandler):

    def initialize(self, authenticator: Authenticator):
        self._authenticator = authenticator

    def get(self):
        self.write(self._authenticator.name)
        self.write("<br/>Hello")


class FaviconHandler(tornado.web.RequestHandler):
    def get(self):
        pass


def make_app():
    # Configure container:
    container = IocContainer()
    container.logger().addHandler(logging.StreamHandler(sys.stdout))

    authenticator = container.auth_service()

    return tornado.web.Application([
        (r"/", MainHandler, {"authenticator": authenticator}),
        (r"/favicon.ico", FaviconHandler)
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
