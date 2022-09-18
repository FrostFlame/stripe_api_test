from django import forms
from django.apps import apps
from django.contrib import admin

# Register your models here.
from api.models import Item, Order, Discount, Tax


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'discount', 'taxes']

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


admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
admin.site.register(Discount)
admin.site.register(Tax)
