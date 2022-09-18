from rest_framework import serializers

from api.models import Item, Order, Discount


class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ['url', 'name', 'description', 'price', 'order']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['url', 'name', 'items', 'discount']


class DiscountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Discount
        fields = ['url', 'name', 'percent_off', 'order']
