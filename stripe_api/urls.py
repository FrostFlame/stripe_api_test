"""stripe_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from api import views
from api.views import custom_handler404

router = routers.DefaultRouter()
router.register(r'items', views.ItemViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'discounts', views.DiscountViewSet)
router.register(r'taxes', views.TaxViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('buy/<int:pk>', views.BuyItem.as_view(), name='buy'),
    path('order_bulk/<int:pk>', views.BuyOrder.as_view(), name='bulk'),
    path('item/<int:pk>', views.ItemView.as_view(), name='item'),
    path('order/<int:pk>', views.OrderView.as_view(), name='order'),
    path('success', TemplateView.as_view(template_name='stripe_api/base/success.html'), name='success'),
    path('cancel', TemplateView.as_view(template_name='stripe_api/base/cancel.html'), name='cancel'),
    path('admin/', admin.site.urls),
]

handler404 = custom_handler404
