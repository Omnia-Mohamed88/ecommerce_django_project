# Generated by Django 5.0.3 on 2024-04-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0008_alter_product_productcategory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.URLField(blank=True, null=True),
        ),
    ]