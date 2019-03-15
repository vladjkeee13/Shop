from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from product.managers import CommentManager, CategoryManager, BrandManager, ProductManager


class ProductSizeSubModel(models.Model):

    product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    size = models.ForeignKey('product.Size', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)


class Product(models.Model):

    name = models.CharField(max_length=255)
    gender = models.ForeignKey("product.Gender", on_delete=models.SET_NULL, null=True)
    category = TreeForeignKey("product.Category", on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey('product.Brand', on_delete=models.SET_NULL, null=True)
    image = models.ManyToManyField('product.Image')
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    size = models.ManyToManyField('product.Size', through=ProductSizeSubModel)
    description = models.TextField()

    objects = ProductManager()

    def __str__(self):
        return self.name


class Category(MPTTModel):

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    objects = CategoryManager()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Brand(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    image_logo = models.ForeignKey('product.Image', on_delete=models.SET_NULL, null=True, related_name='image_logo')
    image_women = models.ForeignKey('product.Image', on_delete=models.SET_NULL, null=True, related_name='image_women')
    image_men = models.ForeignKey('product.Image', on_delete=models.SET_NULL, null=True, related_name='image_men')
    image_kids = models.ForeignKey('product.Image', on_delete=models.SET_NULL, null=True, related_name='image_kids')
    order = models.PositiveSmallIntegerField(default=0)

    objects = BrandManager()

    def __str__(self):
        return self.name


class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='replies')

    comment_manager = CommentManager()


class Image(models.Model):

    image = models.ImageField(upload_to='all_images')

    def __str__(self):
        return str(self.image)


class Gender(models.Model):

    GENDER_WOMEN = 0
    GENDER_MEN = 1
    GENDER_UNISEX = 2
    GENDER_KIDS = 3

    GENDER_CHOICES = (
        (GENDER_WOMEN, "Women"),
        (GENDER_MEN, "Men"),
        (GENDER_UNISEX, "Unisex"),
        (GENDER_KIDS, "Kids")
    )

    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, default=GENDER_UNISEX)

    def __str__(self):
        for number in self.GENDER_CHOICES:
            if self.gender == number[0]:
                return number[1]


class Size(models.Model):

    XS = 0
    S = 1
    M = 2
    L = 3
    XL = 4
    XXL = 5

    SIZE_CHOICES = (
        (XS, "XS"),
        (S, "S"),
        (M, "M"),
        (L, "L"),
        (XL, "XL"),
        (XXL, "XXL")
    )

    size = models.PositiveSmallIntegerField(choices=SIZE_CHOICES, default=M)

    def __str__(self):
        for number in self.SIZE_CHOICES:
            if self.size == number[0]:
                return number[1]
