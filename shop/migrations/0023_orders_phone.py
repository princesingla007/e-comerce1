# Generated by Django 5.1.6 on 2025-04-03 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_remove_orders_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=111),
        ),
    ]
