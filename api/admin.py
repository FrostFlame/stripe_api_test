from django import forms
from django.apps import apps
from django.contrib import admin

# Register your models here.
from api.models import Item, Order


# class ItemInline(admin.TabularInline):
#     model = Item
#     raw_id_fields = ('order',)
#     extra = 1


# class OrderAdmin(admin.ModelAdmin):
#     inlines = [
#         ItemInline,
#     ]


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name']

    items = forms.ModelMultipleChoiceField(queryset=Item.objects.all())

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
        self.cleaned_data['items'].update(order=instance)
        return instance


class OrderAdmin(admin.ModelAdmin):
    form = OrderForm


admin.site.register(Item)
admin.site.register(Order, OrderAdmin)
