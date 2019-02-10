from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    category = models.ManyToManyField("product.Category")
    brand = models.ForeignKey('product.Brand', on_delete=models.SET_NULL, null=True)
    image = models.ManyToManyField('product.Image')
    price = models.PositiveSmallIntegerField(default=0)
    size = models.CharField(max_length=255)
    description = models.TextField()


class Category(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)


class Brand(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField()
    image_logo = models.ForeignKey('product.Image', on_delete=models.SET_NULL, null=True)
    image_women = models.ForeignKey('product.Image', on_delete=models.SET_NULL, null=True)
    image_men = models.ForeignKey('product.Image', on_delete=models.SET_NULL, null=True)
    image_kids = models.ForeignKey('product.Image', on_delete=models.SET_NULL, null=True)


class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)


class Image(models.Model):

    image = models.ImageField(upload_to='all_images')
