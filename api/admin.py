from django import forms
from django.apps import apps
from django.contrib import admin

# Register your models here.
from api.models import Item, Order, Discount


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'discount']

    items = forms.ModelMultipleChoiceField(queryset=Item.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        if self.instance:
            if self.instance.items:
                self.fields['items'].initial = self.instance.items.all()
            else:
                self.fields['items'].initial = []

    def save(self, *args, **kwargs):
        instance = super(OrderForm, self).save(commit=False)
        self.fields['items'].initial.update(order=None)
        instance.save()
        self.cleaned_data['items'].update(order=instance)
        return instance


class OrderAdmin(admin.ModelAdmin):
    form = OrderForm


class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = ['name', 'percent_off']

    orders = forms.ModelMultipleChoiceField(queryset=Order.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super(DiscountForm, self).__init__(*args, **kwargs)
        if self.instance:
            if self.instance.orders:
                self.fields['orders'].initial = self.instance.orders.all()
            else:
                self.fields['orders'].initial = []

    def save(self, *args, **kwargs):
        instance = super(DiscountForm, self).save(commit=False)
        self.fields['orders'].initial.update(discount=None)
        instance.save()
        self.cleaned_data['orders'].update(discount=instance)
        return instance


class DiscountAdmin(admin.ModelAdmin):
    form = DiscountForm


admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(Discount, DiscountAdmin)
