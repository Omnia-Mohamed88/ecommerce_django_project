# Generated by Django 5.0.3 on 2024-04-08 18:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_order_status_alter_order_shipping_status'),
        ('shipping_address', '0003_remove_shippingaddress_order_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_address',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shipping_address.shippingaddress'),
        ),
    ]