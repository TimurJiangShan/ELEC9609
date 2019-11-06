from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    """
    User Profile
    """
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name="name")
    birthday = models.DateField(null=True, blank=True, verbose_name="birthday")
    gender = models.CharField(max_length=6, choices=(("male", "Male"), ("female", "Female")), default="female",
                              verbose_name="gender")
    mobile = models.CharField(null=True, blank=True, max_length=11, verbose_name="mobile")
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name="email")

    class Meta:
        verbose_name = "UserProfile"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    Verify Code
    """
    code = models.CharField(max_length=10, verbose_name="code")
    mobile = models.CharField(max_length=11, verbose_name="mobile")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = "VerifyCode"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
