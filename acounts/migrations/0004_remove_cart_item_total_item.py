# Generated by Django 4.1.2 on 2022-10-21 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acounts', '0003_cart_item_quantity_alter_cart_item_total_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_item',
            name='total_item',
        ),
    ]
