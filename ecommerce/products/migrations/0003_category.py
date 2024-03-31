# Generated by Django 5.0.3 on 2024-03-31 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_rename_products_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("categoryname", models.CharField(max_length=30)),
                ("image", models.ImageField(blank=True, null=True, upload_to="")),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
