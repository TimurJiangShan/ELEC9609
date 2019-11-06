from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from goods.models import Goods

User = get_user_model()


# Create your models here.


class ShoppingCart(models.Model):
    """
    ShoppingCart
    """
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name="goods", on_delete=models.CASCADE)
    nums = models.IntegerField(default=0, verbose_name="nums")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = 'ShoppingCart'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.nums)


class OrderInfo(models.Model):
    """
    Order Info
    """
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "TRADE_SUCCESS"),
        ("TRADE_CLOSED", "TRADE_CLOSED"),
        ("PAYING", "PAYING"),
    )

    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name="order_sn")
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name="trade_no")
    pay_status = models.CharField(choices=ORDER_STATUS, default="paying", max_length=30, verbose_name="pay_status")
    post_script = models.CharField(max_length=200, verbose_name="post_script")
    order_mount = models.FloatField(default=0.0, verbose_name="order_mount")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name="pay_time")

    # 用户信息
    address = models.CharField(max_length=100, default="", verbose_name="address")
    signer_name = models.CharField(max_length=20, default="", verbose_name="signer_name")
    singer_mobile = models.CharField(max_length=11, verbose_name="singer_mobile")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    """
    Order Goods
    """
    order = models.ForeignKey(OrderInfo, verbose_name="order", related_name="goods", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name="goods", on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=0, verbose_name="goods_num")

    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = "OrderGoods"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)
