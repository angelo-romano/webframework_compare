import tornado.ioloop
from tornado import template
from triplander2.base import Application, RequestHandler
from triplander2.models import City, Country

class CountryListHandler(RequestHandler):
    def get(self):
        countries = sorted(self.db.query(Country).all(), key=lambda o: o.name)
        self.render('country_list.html', countries=countries)

class CountryHandler(RequestHandler):
    def get(self, country_slug):
        country = self.db.query(Country).filter_by(slug=country_slug).first()
        self.render('country.html', country=country)

class CityListHandler(RequestHandler):
    def get(self, country_slug):
        country = self.db.query(Country).filter_by(slug=country_slug).first()
        self.render('city_list.html', country=country)

class CityHandler(RequestHandler):
    def get(self, country_slug, city_slug):
        city = self.db.query(City).filter_by(slug=city_slug).first()
        self.render('city.html', city=city)

if __name__ == '__main__':
    app = Application([
        (r"/countries/(.*)/cities/(.*)/", CityHandler),
        (r"/countries/(.*)/cities/", CityListHandler),
        (r"/countries/(.*)/", CountryHandler),
        (r"/countries/", CountryListHandler),
    ])
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
