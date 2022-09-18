from rest_framework import serializers

from api.models import Item, Order, Discount, Tax


class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ['url', 'name', 'description', 'price', 'order']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['url', 'name', 'items', 'discount', 'taxes']


class DiscountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Discount
        fields = ['url', 'name', 'percent_off', 'order']


class TaxSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tax
        fields = ['url', 'name', 'percentage', 'is_inclusive', 'orders']
