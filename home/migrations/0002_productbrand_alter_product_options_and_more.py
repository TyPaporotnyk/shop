# Generated by Django 4.2 on 2023-05-11 17:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductBrand",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Название")),
                (
                    "alternative_name",
                    models.CharField(
                        max_length=50, verbose_name="Альтернативное название"
                    ),
                ),
            ],
            options={
                "verbose_name": "Брэнд",
                "verbose_name_plural": "Брэнды",
            },
        ),
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("-created_at",),
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
        migrations.AlterModelOptions(
            name="producttype",
            options={
                "verbose_name": "Тип товара",
                "verbose_name_plural": "Типы товаров",
            },
        ),
    ]