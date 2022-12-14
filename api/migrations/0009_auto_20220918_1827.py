# Generated by Django 3.2.15 on 2022-09-18 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20220918_1750'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название налога')),
                ('is_inclusive', models.BooleanField(default=False, verbose_name='Включён?')),
                ('percentage', models.IntegerField(verbose_name='Процент налога')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='tax',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='orders', to='api.tax'),
        ),
    ]
