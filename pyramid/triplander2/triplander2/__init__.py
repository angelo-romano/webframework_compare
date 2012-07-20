from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import DBSession

routes = frozenset([
    ('country_list', '/countries/'),
    ('country', '/countries/{country_slug}/'),
    ('city_list', '/countries/{country_slug}/cities/'),
    ('city', '/countries/{country_slug}/cities/{city_slug}/'),
])

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    for (route_name, route_uri) in routes:
        config.add_route(route_name, route_uri)
    config.scan()
    return config.make_wsgi_app()

