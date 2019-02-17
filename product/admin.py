from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from product.models import Product, Category, Brand, Image, Size, Gender


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'gender', 'price')
    search_fields = ('brand__name', )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Brand)
admin.site.register(Image)
admin.site.register(Size)
admin.site.register(Gender)
