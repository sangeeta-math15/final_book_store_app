from django.db import models

# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=10, unique=False)
    is_verified = models.BooleanField(default=False)

    def get_email(self):
        return self.email

    def __str__(self):
        return self.email


class UserOTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_st = models.DateTimeField(auto_now=True)
    otp = models.BigIntegerField()
