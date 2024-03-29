from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(max_length=150, unique=True, verbose_name='почта')
    phone = models.CharField(max_length=35, verbose_name='Телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    telegram = models.CharField(max_length=20, verbose_name='Телеграм', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
