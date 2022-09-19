"""Модели и формы для джанго-админки"""
from django import forms
from django.contrib import admin

# Register your models here.
from api.models import Item, Order, Discount, Tax


class OrderForm(forms.ModelForm):
    """Форма модели заказов для джанго-админки"""
    class Meta:
        """Мета-класс."""
        model = Order
        fields = ['name', 'discount', 'taxes']

    items = forms.ModelMultipleChoiceField(
        queryset=Item.objects.all(),
        required=False
    )

    def __init__(self, *args, **kwargs):
        """Инициализация."""
        super(OrderForm, self).__init__(*args, **kwargs)
        if self.instance:
            if self.instance.items:
                self.fields['items'].initial = self.instance.items.all()
            else:
                self.fields['items'].initial = []

    def save(self, *args, **kwargs):
        """Сохранение связей с товарами через заказ."""
        instance = super(OrderForm, self).save(commit=False)
        self.fields['items'].initial.update(order=None)
        instance.save()
        self.cleaned_data['items'].update(order=instance)
        return instance


class OrderAdmin(admin.ModelAdmin):
    """Админ-модель заказов"""
    form = OrderForm


class DiscountForm(forms.ModelForm):
    """Форма модели скидок для джанго-админки."""
    class Meta:
        """Мета-класс."""
        model = Discount
        fields = ['name', 'percent_off']

    orders = forms.ModelMultipleChoiceField(
        queryset=Order.objects.all(),
        required=False
    )

    def __init__(self, *args, **kwargs):
        """Иниуиализация."""
        super(DiscountForm, self).__init__(*args, **kwargs)
        if self.instance:
            if self.instance.orders:
                self.fields['orders'].initial = self.instance.orders.all()
            else:
                self.fields['orders'].initial = []

    def save(self, *args, **kwargs):
        """Сохранение связей с заказами через скидки."""
        instance = super(DiscountForm, self).save(commit=False)
        self.fields['orders'].initial.update(discount=None)
        instance.save()
        self.cleaned_data['orders'].update(discount=instance)
        return instance


class DiscountAdmin(admin.ModelAdmin):
    """Админ-модель скидок."""
    form = DiscountForm


admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Tax)
