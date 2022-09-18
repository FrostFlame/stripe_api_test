# Generated by Django 3.2.15 on 2022-09-18 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_discount_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discount',
            name='order',
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='api.discount'),
        ),
    ]