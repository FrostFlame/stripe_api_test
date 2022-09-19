"""Модели приложения api."""
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Item(models.Model):
    """Модель Товара"""

    class YearInSchool(models.TextChoices):
        """Список значений валют."""
        RUB = 'RUB', _('Ruble')
        USD = 'USD', _('US Dollar')

    name = models.CharField(max_length=50, verbose_name='Название товара')
    description = models.CharField(max_length=300, verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    order = models.ForeignKey(
        'Order',
        related_name='items',
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True
    )
    currency = models.CharField(
        max_length=3,
        choices=YearInSchool.choices,
        default=YearInSchool.RUB
    )

    def __str__(self):
        """Строковое представление."""
        return self.name


class Order(models.Model):
    """Модель заказа, объединяющего несколько товаров, скидки и налоги."""
    name = models.CharField(max_length=50, verbose_name='Название заказа')
    discount = models.ForeignKey(
        'Discount',
        related_name='orders',
        on_delete=models.DO_NOTHING,
        null=True, blank=True
    )
    taxes = models.ManyToManyField('Tax', related_name='orders', blank=True)

    def __str__(self):
        """Строковое представление."""
        return self.name


class Discount(models.Model):
    """Содель скидок."""
    name = models.CharField(max_length=50, verbose_name='Название скидки')
    percent_off = models.IntegerField(verbose_name='Процент скидки')

    def __str__(self):
        """Строковое представление."""
        return self.name


class Tax(models.Model):
    """Модель налогов."""
    class Meta:
        """Множественное число."""
        verbose_name_plural = "taxes"

    name = models.CharField(max_length=50, verbose_name='Название налога')
    is_inclusive = models.BooleanField(default=False, verbose_name='Включён?')
    percentage = models.IntegerField(verbose_name='Процент налога')

    def __str__(self):
        """Строковое представление."""
        return self.name
