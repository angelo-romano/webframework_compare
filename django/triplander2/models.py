from django.db import models


class Country(models.Model):
    class Meta:
        db_table = 'countries'

    wikiname = models.CharField(max_length=96)
    slug = models.CharField(max_length=32)
    name = models.CharField(max_length=96)
    code = models.CharField(max_length=5)
    currency = models.CharField(max_length=32)

 
class City(models.Model):
    class Meta:
        db_table = 'cities'

    wikiname = models.CharField(max_length=96)
    slug = models.CharField(max_length=32)
    name = models.CharField(max_length=96)
    rankings_1 = models.FloatField()
    rankings_2 = models.FloatField()
    rankings_3 = models.FloatField()
    rankings_4 = models.FloatField()
    total_ranking = models.FloatField()
    timezone = models.CharField(max_length=16)
    latitude = models.FloatField()
    longitude = models.FloatField()
    country = models.ForeignKey(Country)

