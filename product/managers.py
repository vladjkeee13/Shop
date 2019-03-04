from django.db.models import Manager


class CommentManager(Manager):

    def get_comment_by_product(self, product):
        return self.get_queryset().filter(parent__isnull=True, product=product)


class CategoryManager(Manager):

    def get_gender_category_by_name(self, name):
        return self.get_queryset().get(name=name)


class BrandManager(Manager):

    def get_brand_by_name(self, name):
        return self.get_queryset().get(name=name)


class ProductManager(Manager):

    def get_product_by_category_and_brand(self, category, brand):
        return self.get_queryset().filter(category=category, brand=brand)
