from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods

# Create your models here.
User = get_user_model()


class UserFav(models.Model):
    """
    User Fav
    """
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name="goods", help_text="goods id", on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = 'UserFav'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return self.user.name


class UserLeavingMessage(models.Model):
    """
    User Leaving Message
    """
    MESSAGE_CHOICES = (
        (1, "Leave message"),
        (2, "complain"),
        (3, "ask for help"),
        (4, "service"),
        (5, "ask for goods")
    )
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    message_type = models.IntegerField(default=1, choices=MESSAGE_CHOICES, verbose_name="message_type",
                                       help_text="MESSAGE CHOICES: 1(Leave message),2(complain),3(ask for help),"
                                                 "4(service),5(ask for goods)")
    subject = models.CharField(max_length=100, default="", verbose_name="subject")
    message = models.TextField(default="", verbose_name="message", help_text="message context")
    file = models.FileField(upload_to="message/images/", verbose_name="file", help_text="file")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = "UserLeavingMessage"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.subject


class UserAddress(models.Model):
    """
    User Address
    """
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    province = models.CharField(max_length=100, default="", verbose_name="province")
    city = models.CharField(max_length=100, default="", verbose_name="city")
    district = models.CharField(max_length=100, default="", verbose_name="district")
    address = models.CharField(max_length=100, default="", verbose_name="address")
    signer_name = models.CharField(max_length=100, default="", verbose_name="signer_name")
    signer_mobile = models.CharField(max_length=11, default="", verbose_name="signer_mobile")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = "UserAddress"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.address
