from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Cart(models.Model):

    product = models.ManyToManyField('product.Product')
    quantity = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)


class Wishlist(models.Model):

    product = models.ManyToManyField('product.Product')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
