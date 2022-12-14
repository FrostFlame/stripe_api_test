"""Представления приложения api."""
from functools import reduce

import stripe
from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from api.models import Item
from api.models import Order
from api.models import Discount
from api.models import Tax
from api.serializers import ItemSerializer
from api.serializers import OrderSerializer
from api.serializers import DiscountSerializer
from api.serializers import TaxSerializer
from stripe_api.settings import STRIPE_API_KEY
from stripe_api.settings import STRIPE_PUBLISHABLE_KEY

stripe.api_key = STRIPE_API_KEY


class BuyItem(APIView):
    """
    View для покупки итема.
    """

    def get(self, request, pk):
        """
        Возвращает Stripe Session Id для оплаты выбранного Item.
        /buy/{id}
        """
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response('Item с таким id не существует.')
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel',
        )
        return Response(session.stripe_id)


class ItemViewSet(viewsets.ModelViewSet):
    """
    View для drf-api модели товаров.
    /items
    /items/{id}
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemView(APIView):
    """
    View страницы товара.
    /item/{id}
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'stripe_api/base/item.html'

    def get(self, request, pk):
        """Страница товара."""
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return custom_handler404(request, 'ads')
        return Response({
            'item': item,
            'STRIPE_PUBLISHABLE_KEY': STRIPE_PUBLISHABLE_KEY
        })


def custom_handler404(request, exception):
    """Хэндлер 404 ошибки"""
    return render(request, "stripe_api/base/404.html", status=404)


class OrderViewSet(viewsets.ModelViewSet):
    """
    View для drf-api модели заказов.
    /orders
    /orders/{id}"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class BuyOrder(APIView):
    """View для покупки всего заказа."""
    def get(self, request, pk):
        """
        Возвращает Stripe Session Id для оплаты выбранного Order.
        /order_bulk/{id}
        """
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response('Order с таким id не существует.')
        items = order.items.all()
        if not items:
            return Response('Данный Order не содержит Items"')
        line_items = []
        for item in items:
            line_items.append({
                'price_data': {
                    'currency': item.currency,
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(item.price * 100),
                },
                'quantity': 1,
            })
        discounts = []
        if order.discount:
            coupon = stripe.Coupon.create(
                percent_off=order.discount.percent_off,
                duration='once',
                name=order.discount.name
            )
            discounts = [{'coupon': coupon.id}]
        if order.taxes:
            line_items[0]['tax_rates'] = [
                stripe.TaxRate.create(
                    display_name=tax.name,
                    inclusive=tax.is_inclusive,
                    percentage=tax.percentage
                ).id for tax in order.taxes.all()
            ]
        session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            discounts=discounts,
            success_url='http://localhost:8000/success',
            cancel_url='http://localhost:8000/cancel',
        )
        return Response(session.stripe_id)


class OrderView(APIView):
    """View страницы заказа."""
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'stripe_api/base/order.html'

    def get(self, request, pk):
        """
        Страница заказа.
        /order/{id}
        """
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return custom_handler404(request, 'ads')
        same_currency = reduce(
            lambda x, y: x == y,
            [item.currency for item in order.items.all()]
        )
        return Response({
            'order': order,
            'STRIPE_PUBLISHABLE_KEY': STRIPE_PUBLISHABLE_KEY,
            'same_currency': same_currency
        })


class DiscountViewSet(viewsets.ModelViewSet):
    """
    View для drf-api модели скидок.
    /discounts
    /discounts/{id}
    """
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer


class TaxViewSet(viewsets.ModelViewSet):
    """
    View для drf-api модели налогов.
    /taxes
    /taxes/{id}
    """
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer
