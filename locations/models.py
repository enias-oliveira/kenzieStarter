from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=255)
    localized_name = models.CharField(max_length=255)
    country = models.CharField(max_length=2)
    country_full = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
