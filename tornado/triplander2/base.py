import tornado.web
import tornado.template
from triplander2.models import engine
from sqlalchemy.orm import scoped_session, sessionmaker

class Application(tornado.web.Application):
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.db = scoped_session(sessionmaker(bind=engine))

class RequestHandler(tornado.web.RequestHandler):
    loader = tornado.template.Loader('./triplander2/templates')
    @property
    def db(self):
        return self.application.db

    def render(self, template, **kwargs):
        self.write(self.loader.load(template).generate(**kwargs))
