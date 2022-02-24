from django.db import models
from user.models import User


class Book(models.Model):
    """
    create Book model
    """
    author = models.CharField(max_length=15)
    title = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField()
    price = models.IntegerField()
    description = models.CharField(max_length=150)

