# Generated by Django 4.2.16 on 2024-10-16 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="description",
            field=models.CharField(max_length=300, null=True),
        ),
    ]
