from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    
    username = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255, null=False)

    # avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

