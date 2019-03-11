from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from cart.models import Cart, CartItem
from product.models import Product, Category, Brand, Image, Size, Gender, ProductSizeSubModel, Comment


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'gender', 'price')
    search_fields = ('brand__name', )


class ProductSizeSubModelAdmin(admin.ModelAdmin):
    list_display = ('product', 'size', 'count')


# class SizeAdmin(admin.ModelAdmin):
#     list_display = ('label', 'category', 'gender')


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order', )


class CustomMPTTModelAdmin(MPTTModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'product', 'parent')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CustomMPTTModelAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Image)
admin.site.register(Size)
admin.site.register(Gender)
admin.site.register(ProductSizeSubModel, ProductSizeSubModelAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CartItem)
admin.site.register(Cart)
