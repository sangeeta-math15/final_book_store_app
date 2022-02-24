from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    This model has default athentication
    """
    name = models.CharField(max_length=15, unique=False)
    phone = models.CharField(max_length=10, unique=False)
    is_verified = models.BooleanField(default=False)



class UserOTP(models.Model):
    """
    create UserOTP model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_st = models.DateTimeField(auto_now=True)
    otp = models.BigIntegerField()
