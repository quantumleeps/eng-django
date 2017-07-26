from django.db import models

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    shortname = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Group(models.Model):
    description = models.CharField(max_length=200)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    def __str__(self):
        return self.description

class Point(models.Model):
    description = models.CharField(max_length=200)
    units = models.CharField(max_length=200)
    tagnum = models.CharField(max_length=200)
    limlow = models.CharField(max_length=200)
    limhigh = models.CharField(max_length=200)
    limlowlow = models.CharField(max_length=200)
    limhighhigh = models.CharField(max_length=200)
    required = models.BooleanField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)