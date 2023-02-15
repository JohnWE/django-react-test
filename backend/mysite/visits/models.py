from django.db import models


class CurrentVisits(models.Model):
    country = models.CharField(max_length=50)
    visits = models.IntegerField()
