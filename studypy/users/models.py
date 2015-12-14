from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(verbose_name='image', upload_to='profile_images',
                              blank=True, null=True)

