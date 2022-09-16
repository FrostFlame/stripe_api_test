import stripe
from django.shortcuts import render
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from api.models import Item
from api.serializers import ItemSerializer
from stripe_api.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


class BuyItem(APIView):
    """
    View для покупки итема.
    """

    def get(self, request, pk):
        """
        Возвращает Stripe Session Id для оплаты выбранного Item
        """
        try:
            item = Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return Response('Item с таким id не существует.')
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'rub',
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
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'stripe_api/base/item.html'

    def get(self, request, pk):
        item = Item.objects.get(pk=pk)
        return Response({'item': item})


def custom_handler404(request, exception):
    return render(request, "stripe_api/base/404.html", status=404)
