# Generated by Django 4.2.16 on 2024-10-21 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0004_sale"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sale", old_name="date_added", new_name="date_sold",
        ),
    ]