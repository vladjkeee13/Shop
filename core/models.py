from django.db import models


class Feedback(models.Model):

    email = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
