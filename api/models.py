from django.db import models

# Create your models here.


class Item(models.Model):
    """Модель Item"""
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=300, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    order = models.ForeignKey('Order', related_name='items', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')

    def __str__(self):
        return self.name
