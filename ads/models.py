from django.db import models


# Create your models here.
class Ads(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    is_published = models.BooleanField(default=False)


class Categories(models.Model):
    id = models.IntegerField(primary_key=True, unique=True, auto_created=True)
    name = models.CharField(max_length=150)
