# Generated by Django 3.2.15 on 2022-09-18 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_rename_tax_order_taxes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='taxes',
            field=models.ManyToManyField(blank=True, related_name='orders', to='api.Tax'),
        ),
    ]