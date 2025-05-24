from django.db import models

from .user import User


class Meeting(models.Model):
    date = models.DateField()
    employees = models.ManyToManyField(User)
