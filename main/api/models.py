from django.db import models
from django.db.models import CharField, IntegerField, ForeignKey


class Location(models.Model):
    title = CharField(max_length=200, unique=True)
    locality = CharField(max_length=200)
    administrative_area_level_3 = CharField(max_length=200)
    administrative_area_level_3_short = CharField(max_length=5)
    administrative_area_level_2 = CharField(max_length=200)
    administrative_area_level_1 = CharField(max_length=200)
    administrative_area_level_1_short = CharField(max_length=5)
    country = CharField(max_length=200)
    country_short = CharField(max_length=3)
    lat = models.FloatField()
    long = models.FloatField()


class Datum(models.Model):
    title = CharField(max_length=100)
    infected = IntegerField()
    deaths = IntegerField()
    recovered = IntegerField()
    location = ForeignKey(Location, on_delete=models.CASCADE)
