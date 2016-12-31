import tornado.ioloop
import tornado.web
from tornado.escape import json_encode

from DataDumping import *
from SearchCongress import *

sqlite3_connection = sqlite3.connect('../database/republic.db')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class CongressHandler(tornado.web.RequestHandler):
    def get(self):
        state = str(self.get_argument('state'))
        congressmen_type = str(self.get_argument('congressmen_type'))
        csearch = CongressSearch(sqlite3_connection)
        res = csearch.search_by_state(state, congressmen_type)
        self.write(json_encode(res))


def make_app():
    return tornado.web.Application([
        (r"/congress", CongressHandler),
    ])


def start_server():
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()