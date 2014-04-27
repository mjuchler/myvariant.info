'''
A thin python layer for accessing GeneDoc ElasticSearch host.

Currently available URLs:

    /query?q=cdk2      gene query service
    /gene/<geneid>     gene annotation service

'''
import sys
import os.path
import subprocess
import json

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.escape
from tornado.options import define, options

src_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
if src_path not in sys.path:
    sys.path.append(src_path)
#from config import INCLUDE_DOCS
#from utils.es import ESQuery
from helper import add_apps, BaseHandler
from api.handlers import APP_LIST as api_app_list


__USE_WSGI__ = False
#DOCS_STATIC_PATH = os.path.join(src_path, 'docs/_build/html')
#if INCLUDE_DOCS and not os.path.exists(DOCS_STATIC_PATH):
#    raise IOError('Run "make html" to generate sphinx docs first.')
STATIC_PATH = os.path.join(src_path, 'src/static')

define("port", default=8000, help="run on the given port", type=int)
define("address", default="127.0.0.1", help="run on localhost")
define("debug", default=False, type=bool, help="run in debug mode")
tornado.options.parse_command_line()
if options.debug:
    import tornado.autoreload
    import logging
    logging.getLogger().setLevel(logging.DEBUG)
    options.address = '0.0.0.0'



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        #if INCLUDE_DOCS:
            self.render(os.path.join(DOCS_STATIC_PATH, 'index.html'))




APP_LIST = [
    (r"/", MainHandler),
]

APP_LIST += add_apps('api', api_app_list)


settings = {}
if options.debug:
#     from config import STATIC_PATH
    settings.update({
        "static_path": STATIC_PATH,
    })
#    from config import auth_settings
#    settings.update(auth_settings)
print APP_LIST

def main():
    application = tornado.web.Application(APP_LIST, **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port, address=options.address)
    loop = tornado.ioloop.IOLoop.instance()
    if options.debug:
        tornado.autoreload.start(loop)
        logging.info('Server is running on "%s:%s"...' % (options.address, options.port))


    loop.start()


if __name__ == "__main__":
    main()