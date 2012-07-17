from triplander2.base import app
from triplander2.models import Country, City
from flask import render_template

@app.route('/countries/')
def list_countries():
    countries = Country.query.all()
    return render_template('country_list.html', countries=countries)


@app.route('/countries/<country_slug>/')
def show_country(country_slug):
    country = Country.query.filter_by(slug=country_slug).first()
    return render_template('country.html', country=country)


@app.route('/countries/<country_slug>/cities/')
def list_country_cities(country_slug):
    country = Country.query.filter_by(slug=country_slug).first()
    return render_template('city_list.html', country=country)


@app.route('/countries/<country_slug>/cities/<city_slug>')
def show_city(country_slug):
    city = City.query.filter_by(slug=city_slug).first()
    return render_template('city.html', city=city)


if __name__ == '__main__':
    app.run(debug=True)
