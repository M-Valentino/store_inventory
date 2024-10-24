# Generated by Django 4.2.16 on 2024-10-22 21:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0005_rename_date_added_sale_date_sold"),
    ]

    operations = [
        migrations.CreateModel(
            name="Restock",
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
                ("product_id", models.IntegerField()),
                ("restock_qty", models.IntegerField()),
                (
                    "date_restocked",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
    ]
