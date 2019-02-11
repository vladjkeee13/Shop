from django.contrib import admin

from product.models import Product, Category, Brand, Image

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Image)
