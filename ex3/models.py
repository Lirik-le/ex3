from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=255, verbose_name='Логин', unique=True, blank=False)
    image = models.ImageField(upload_to='user', verbose_name='Аватарка', blank=False)
    first_name = models.CharField(max_length=255, verbose_name='Имя', blank=False)
    last_name = models.CharField(max_length=255, verbose_name='Фамилия', blank=False)
    password = models.CharField(max_length=255, verbose_name='Пароль', blank=False)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.first_name


class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название', blank=False)
    image = models.ImageField(upload_to='item', verbose_name='Картинка', blank=False)
    description = models.TextField(max_length=1000, verbose_name='Описание', blank=True)

    def __str__(self):
        return self.title
