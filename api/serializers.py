from rest_framework import serializers

from api.models import Item, Order


class ItemSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ['url', 'name', 'description', 'price']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['url', 'name', 'items']
