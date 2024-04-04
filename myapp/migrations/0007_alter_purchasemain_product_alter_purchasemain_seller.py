# Generated by Django 5.0.3 on 2024-04-02 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0006_sellerordermain_sellerordersub"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchasemain",
            name="PRODUCT",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.products"
            ),
        ),
        migrations.AlterField(
            model_name="purchasemain",
            name="SELLER",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.seller"
            ),
        ),
    ]