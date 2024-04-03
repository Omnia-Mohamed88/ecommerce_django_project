# Generated by Django 5.0.3 on 2024-03-31 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="productcategory",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product",
                to="products.category",
            ),
        ),
    ]