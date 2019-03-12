# Django
from django.db import models


class Task(models.Model):
    """
    Task model
    """

    title = models.CharField(max_length=75)
    description = models.TextField()
