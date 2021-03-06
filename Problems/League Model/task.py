from django.db import models
from django.db.models import CharField, ForeignKey, IntegerField


class Team(models.Model):
    name = models.CharField(max_length=64)
    champion_of = models.CharField(max_length=48)

    class Meta:
        app_label = 'tournament'


class League(models.Model):
    name = models.CharField(max_length=32)
    number_of_teams = models.IntegerField()
    champion = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        app_label = 'tournament'
