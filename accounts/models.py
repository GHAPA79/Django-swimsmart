from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, blank=True)
    phone_number = models.CharField(max_length=12, unique=True)
