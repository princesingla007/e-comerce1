# Generated by Django 5.1.6 on 2025-04-04 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_rename_email_orders_phone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
