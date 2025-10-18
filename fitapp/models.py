from django.conf import settings
from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    created_date = models.DateTimeField(
            default=timezone.now)
