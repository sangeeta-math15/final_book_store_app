from django.db import models


# Create your models here.
class Book(models.Model):
    author = models.CharField(max_length=15)
    title = models.CharField(max_length=30)
    quantity = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=150)

