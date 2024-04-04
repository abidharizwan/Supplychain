# Generated by Django 5.0.3 on 2024-04-04 08:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp", "0008_productordermain_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="sellerproducts",
            old_name="modelnumber",
            new_name="quantity",
        ),
        migrations.RemoveField(
            model_name="sellerproducts",
            name="category",
        ),
        migrations.RemoveField(
            model_name="sellerproducts",
            name="description",
        ),
        migrations.RemoveField(
            model_name="sellerproducts",
            name="measurement",
        ),
        migrations.RemoveField(
            model_name="sellerproducts",
            name="productname",
        ),
        migrations.RemoveField(
            model_name="sellerproducts",
            name="sellerid",
        ),
        migrations.AddField(
            model_name="sellerproducts",
            name="PURCHASESUB",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="myapp.purchasesub",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sellerproducts",
            name="saleamount",
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="sellerproducts",
            name="status",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Cart",
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
                ("date", models.DateTimeField()),
                ("quantity", models.IntegerField()),
                (
                    "PRODUCTS",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.sellerproducts",
                    ),
                ),
                (
                    "USER",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.user"
                    ),
                ),
            ],
        ),
    ]
