# Generated by Django 5.1.3 on 2025-01-26 11:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0001_initial"),
        ("store", "0002_variation"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartitem",
            name="variations",
            field=models.ManyToManyField(blank=True, to="store.variation"),
        ),
    ]
