from django.contrib.auth.models import User
from django.db import models


class Cart(models.Model):

    product = models.ManyToManyField('product.Product')
    quantity = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Wishlist(models.Model):

    product = models.ManyToManyField('product.Product')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
