from django.contrib.auth.models import AbstractUser
from django.db import models


class Feedback(models.Model):

    email = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class MyUser(AbstractUser):

    avatar = models.ImageField(blank=True, null=True, upload_to='avatars')
    phone = models.CharField(max_length=255, blank=True, null=True)
