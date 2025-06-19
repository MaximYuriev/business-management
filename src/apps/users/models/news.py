from django.db import models

from .user import User


class News(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
