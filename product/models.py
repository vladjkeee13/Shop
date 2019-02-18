from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


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
    price = models.PositiveSmallIntegerField(default=0)
    size = models.ManyToManyField('product.Size', through=ProductSizeSubModel)
    description = models.TextField()

    def __str__(self):
        return self.name

    # def get_prent_array(self, category):
    #     end = False
    #     while end == False:
    #
    #
    # def save(self, *args, **kwargs):
    #     self.name = "Other name"
    #     #parent_category_id = self.category.get().parent_id
    #     for category in self.category.all():
    #         parent_id = category.parent_id
    #
    #
    #
    #     super(Product, self).save()
    #


class Category(MPTTModel):

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

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

    def __str__(self):
        return self.name


class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)


class Image(models.Model):

    image = models.ImageField(upload_to='all_images')


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

    label = models.CharField(max_length=255)
    category = TreeForeignKey("product.Category", on_delete=models.SET_NULL, null=True)
    gender = models.ForeignKey('Gender', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.label
