from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)