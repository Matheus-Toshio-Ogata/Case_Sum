from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)


class Blotter(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    ticker = models.CharField(max_length=200)
    volume = models.IntegerField()
    price = models.IntegerField()
