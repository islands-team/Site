from django.db import models

# Create your models here.
class User(models.Model):
    ima = models.CharField('Фамилия', max_length=50)
    familia = models.CharField('Имя', max_length=50)
    pochta = models.CharField('Почта', max_length=100)
    password = models.CharField('Пароль', max_length=100)

    def __str__(self):
        return self.pochta