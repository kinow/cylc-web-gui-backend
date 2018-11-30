import tornado.ioloop
import tornado.web

from auth import Authenticator


class MainHandler(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)
        self._authenticator = None

    def initialize(self, authenticator: Authenticator):
        self._authenticator = authenticator

    def get(self):
        self.write(str(self._authenticator))
        self.write("<br/>Hello")


class FaviconHandler(tornado.web.RequestHandler):
    def get(self):
        pass


def make_app():
    authenticator = None
    return tornado.web.Application([
        (r"/", MainHandler, {"authenticator": authenticator}),
        (r"/favicon.ico", FaviconHandler)
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
