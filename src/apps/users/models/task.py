from django.db import models

from .user import User


class Task(models.Model):
    class StatusChoice(models.TextChoices):
        COMPLETED = "completed"
        NOT_COMPLETED = "not completed"

    title = models.CharField(max_length=128)
    description = models.TextField()
    author = models.ForeignKey(User, related_name="created_tasks", on_delete=models.PROTECT)
    responsible = models.ForeignKey(User, related_name="responsible_tasks", on_delete=models.PROTECT)
    status = models.CharField(choices=StatusChoice, max_length=16)
    deadline = models.DateField()
