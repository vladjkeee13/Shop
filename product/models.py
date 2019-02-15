from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=255)
    gender = models.ForeignKey("product.Gender", on_delete=models.SET_NULL, null=True)
    category = models.ManyToManyField("product.Category")
    brand = models.ForeignKey('product.Brand', on_delete=models.SET_NULL, null=True)
    image = models.ManyToManyField('product.Image')
    price = models.PositiveSmallIntegerField(default=0)
    size = models.ForeignKey('product.Size', on_delete=models.SET_NULL, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Category(models.Model):

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

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
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    gender = models.ForeignKey('Gender', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.label
