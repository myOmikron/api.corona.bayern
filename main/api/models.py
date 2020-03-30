from django.db import models
from django.db.models import CharField, IntegerField, ForeignKey, DateField, FloatField


class County(models.Model):
    name = CharField(max_length=40, unique=True, default="")


class Datum(models.Model):
    date = DateField()
    cases = IntegerField(default=0)
    cases_per_100k = FloatField(default=0)
    cases_per_population = FloatField(default=0)
    deaths = IntegerField(default=0)
    death_rate = FloatField(default=0)
    county = ForeignKey(County, on_delete=models.CASCADE)
    county_population = IntegerField(default=0)
