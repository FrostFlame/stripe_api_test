from django.db import models

# Create your models here.


class Item(models.Model):
    """Модель Item"""
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=300, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        print(self.name)
