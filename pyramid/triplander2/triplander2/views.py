from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    City,
    Country,
    )

@view_config(route_name='country_list',
             renderer='triplander2:templates/country_list.mak')
def country_list(request):
    try:
        countries = DBSession.query(Country).all()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'countries': countries}

@view_config(route_name='country',
             renderer='triplander2:templates/country.mak')
def country(request):
    country_slug = request.context.country_slug
    try:
        country = DBSession.query(Country).filter_by(slug=country_slug).first()
    except DBAPIError:
        raise
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'country': country}

@view_config(route_name='city_list',
             renderer='triplander2:templates/city_list.mak')
def city_list(request):
    country_slug = request.context.country_slug
    try:
        country = DBSession.query(Country).filter_by(slug=country_slug).first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'country': country}

@view_config(route_name='city',
             renderer='triplander2:templates/city.mak')
def city(request):
    city_slug = request.context.city_slug
    country_slug = request.context.country_slug
    try:
        city = DBSession.query(City).filter_by(slug=city_slug).first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'city': city}

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_triplander2_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

