from django.db import models
from django.contrib.auth.models import AbstractUser

from .company import Company


class User(AbstractUser):
    class PositionChoice(models.TextChoices):
        MANAGER = "manager"
        SUBORDINATE = "subordinate"

    company = models.ForeignKey(Company, related_name="employees", on_delete=models.PROTECT)
    position = models.CharField(choices=PositionChoice, max_length=16, null=True)
