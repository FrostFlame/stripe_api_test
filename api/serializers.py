"""Сериализаторы для drf."""
from rest_framework import serializers

from api.models import Item, Order, Discount, Tax


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    """Сериализатор модели товаров."""

    class Meta:
        """Мета-класс."""
        model = Item
        fields = ['url', 'name', 'description', 'price', 'currency', 'order']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    """Сериализатор модели заказов."""
    class Meta:
        """Мета-класс."""
        model = Order
        fields = ['url', 'name', 'items', 'discount', 'taxes']


class DiscountSerializer(serializers.HyperlinkedModelSerializer):
    """Сериализатор модели скидок."""
    class Meta:
        """Мета-класс."""
        model = Discount
        fields = ['url', 'name', 'percent_off', 'order']


class TaxSerializer(serializers.HyperlinkedModelSerializer):
    """Сериализатор модели налогов."""
    class Meta:
        """Мета-класс."""
        model = Tax
        fields = ['url', 'name', 'percentage', 'is_inclusive', 'orders']
