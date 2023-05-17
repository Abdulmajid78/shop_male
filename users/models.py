from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    user_image = models.ImageField(upload_to='users/', null=True, blank=True)
