from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.


class GoodsCategory(models.Model):
    """
    Goods Category
    """
    CATEGORY_TYPE = (
        (1, "type 1"),
        (2, "type 2"),
        (3, "type 3"),
    )

    name = models.CharField(default="", max_length=30, verbose_name="category_name", help_text="category name")
    code = models.CharField(default="", max_length=30, verbose_name="category_code", help_text="category code")
    desc = models.TextField(default="", verbose_name="category_description", help_text="category description")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, verbose_name="category_type", help_text="category type")
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="parent_category",
                                        help_text="parent category", related_name="sub_cat", on_delete=models.CASCADE)
    is_tab = models.BooleanField(default=False, verbose_name="is_tab", help_text="is tab")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = "GoodsCategory"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    Goods Category Brand
    """
    category = models.ForeignKey(GoodsCategory, related_name='brands', null=True, blank=True, verbose_name="商品类目",
                                 on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=30, verbose_name="brand_name", help_text="brand name")
    desc = models.TextField(default="", max_length=200, verbose_name="brand_description", help_text="brand description")
    image = models.ImageField(max_length=200, upload_to="brands/")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = "GoodsCategoryBrand"
        verbose_name_plural = verbose_name
        db_table = "goods_goodsbrand"

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    Goods
    """
    category = models.ForeignKey(GoodsCategory, verbose_name="goods_category", on_delete=models.CASCADE)
    goods_sn = models.CharField(max_length=50, default="", verbose_name="goods_sn")
    name = models.CharField(max_length=100, verbose_name="goods_name")
    click_num = models.IntegerField(default=0, verbose_name="click_num")
    sold_num = models.IntegerField(default=0, verbose_name="sold_num")
    fav_num = models.IntegerField(default=0, verbose_name="fav_num")
    goods_num = models.IntegerField(default=0, verbose_name="goods_num")
    market_price = models.FloatField(default=0, verbose_name="market_price")
    shop_price = models.FloatField(default=0, verbose_name="shop_price")
    goods_brief = models.TextField(max_length=500, verbose_name="goods_brief")
    goods_desc = UEditorField(verbose_name="goods_desc", imagePath="goods/images/", width=1000, height=300,
                              filePath="goods/files/", default='')
    ship_free = models.BooleanField(default=True, verbose_name="ship_free")
    goods_front_image = models.ImageField(upload_to="goods/images/", null=True, blank=True,
                                          verbose_name="goods_front_image")
    is_new = models.BooleanField(default=False, verbose_name="is_new")
    is_hot = models.BooleanField(default=False, verbose_name="is_hot")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = 'Goods'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class IndexAd(models.Model):
    """
    Index Ad
    """
    category = models.ForeignKey(GoodsCategory, related_name='category', verbose_name="goods_category",
                                 on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, related_name='goods', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'IndexAd'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class GoodsImage(models.Model):
    """
    Goods Image
    """
    goods = models.ForeignKey(Goods, verbose_name="goods", related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", verbose_name="image", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = 'GoodsImage'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    Banner
    """
    goods = models.ForeignKey(Goods, verbose_name="goods", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banner', verbose_name="image")
    index = models.IntegerField(default=0, verbose_name="index")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    """
    HotSearchWords
    """
    keywords = models.CharField(default="", max_length=20, verbose_name="keywords")
    index = models.IntegerField(default=0, verbose_name="index")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="add_time")

    class Meta:
        verbose_name = 'HotSearchWords'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.keywords
