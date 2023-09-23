from django.contrib.auth.models import AbstractUser
from django.db import models

from mailing.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(max_length=50, unique=True, verbose_name='почта')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

