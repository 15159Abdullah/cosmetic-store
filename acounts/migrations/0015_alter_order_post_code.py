# Generated by Django 4.1.2 on 2022-10-24 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acounts', '0014_remove_order_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='post_code',
            field=models.IntegerField(null=True),
        ),
    ]