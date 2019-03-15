from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class CartItem(models.Model):

    size = models.ForeignKey('product.ProductSizeSubModel', on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return "Cart item for product {0}".format(self.size.product.name)


class Cart(models.Model):

    items = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)

    def add_to_cart(self, size):

        cart = self
        new_item, _ = CartItem.objects.get_or_create(size=size, item_total=size.product.price)

        if new_item not in cart.items.all():
            cart.items.add(new_item)
            cart.save()

    def remove_from_cart(self, item):

        cart = self

        if item in cart.items.all():
            cart.items.remove(item)
            cart.save()


class Wishlist(models.Model):

    product = models.ManyToManyField('product.Product')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
