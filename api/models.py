from django.db import models

# Create your models here.


class Item(models.Model):
    """Модель Item"""
    name = models.CharField(max_length=50, verbose_name='Название товара')
    description = models.CharField(max_length=300, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    order = models.ForeignKey('Order', related_name='items', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название заказа')
    discount = models.ForeignKey('Discount', related_name='orders', on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название скидки')
    percent_off = models.IntegerField(verbose_name='Процент скидки')

    def __str__(self):
        return self.name


# class Tax(models.Model):
#     pass
