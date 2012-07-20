from django.http import HttpResponse
# this one is available from Django 1.3, we'll use render_to_response instead
# from django.template.response import TemplateResponse
from django.shortcuts import render_to_response
from triplander2.models import City, Country

def country_list(request):
    countries = Country.objects.all()
    # sort must be done at this level on Django (unless we create a custom filter)
    countries = sorted(countries, key=lambda x: x.name)
    return render_to_response('country_list.html',
                              {'countries': countries})

def country(request, country_slug):
    country = Country.objects.get(slug=country_slug)
    return render_to_response('country.html',
                              {'country': country})

def city_list(request, country_slug):
    country = Country.objects.get(slug=country_slug)
    return render_to_response('city_list.html',
                              {'country': country,
                               'cities': sorted(country.city_set.all(), key=lambda x: x.name)})

def city(request, country_slug, city_slug):
    city = City.objects.get(slug=city_slug)
    return render_to_response('city.html',
                              {'city': city,
                               'city_longitude_lbound': city.longitude - 0.5,
                               'city_latitude_lbound': city.latitude - 0.5,
                               'city_longitude_ubound': city.longitude + 0.5,
                               'city_latitude_ubound': city.latitude + 0.5})

