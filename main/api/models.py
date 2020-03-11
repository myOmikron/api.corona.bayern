from django.db import models
from django.db.models import CharField, IntegerField, ForeignKey, DateField


class Location(models.Model):
    name = CharField(max_length=40, unique=True, default="")


class Datum(models.Model):
    infected = IntegerField()
    date = DateField(auto_now=True)
#    deaths = IntegerField()
#    recovered = IntegerField()
    location = ForeignKey(Location, on_delete=models.CASCADE)
