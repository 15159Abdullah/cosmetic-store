# Generated by Django 4.1.2 on 2022-10-25 03:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('acounts', '0018_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]