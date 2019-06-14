from django.db import models

class Movie(models.Model):
    name=models.CharField(max_length=4000)
    objects=models.Manager()

class Weather(models.Model):
    wCity=models.CharField(max_length=20)
    wDate=models.CharField(max_length=20)
    wWeather=models.CharField(max_length=20)
    wTemp=models.CharField(max_length=20)
    objects=models.Manager()

class Phones(models.Model):
    mNo=models.CharField(max_length=32)
    mMark=models.CharField(max_length=256)
    mPrice=models.CharField(max_length=32)
    mNote=models.CharField(max_length=1024)
    mFile=models.CharField(max_length=256)
    objects=models.Manager()

class Bags(models.Model):
    price=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    objects=models.Manager()
