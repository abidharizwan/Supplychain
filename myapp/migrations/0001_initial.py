# Generated by Django 5.0.3 on 2024-03-07 03:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("customername", models.CharField(max_length=100)),
                ("type", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("phone", models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Customerordermain",
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
                ("date", models.DateField()),
                ("amount", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Login",
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
                ("username", models.CharField(max_length=100)),
                ("password", models.CharField(max_length=100)),
                ("type", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Products",
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
                ("productname", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                ("unitofmeasurement", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Rawmaterials",
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
                ("name", models.CharField(max_length=100)),
                ("category", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=100)),
                ("origin", models.CharField(max_length=100)),
                ("harvestorproductiondate", models.DateField()),
                ("certification", models.CharField(max_length=250)),
                ("cost", models.CharField(max_length=100)),
                ("quantityavailable", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Sellerorder",
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
                ("orderdate", models.DateField()),
                ("address", models.CharField(max_length=250)),
                ("status", models.CharField(max_length=100)),
                ("totalquantity", models.CharField(max_length=100)),
                ("totalordervalue", models.CharField(max_length=100)),
                ("paymentmethod", models.CharField(max_length=100)),
                ("paymentstatus", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Manufacture",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("phone", models.BigIntegerField()),
                ("website", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("registrationdate", models.DateField()),
                ("status", models.CharField(max_length=100)),
                ("logo", models.CharField(max_length=250)),
                ("certification", models.CharField(max_length=250)),
                (
                    "LOGIN",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.login"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Manufactureproducts",
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
                ("productname", models.CharField(max_length=250)),
                ("category", models.CharField(max_length=250)),
                ("description", models.CharField(max_length=250)),
                ("specification", models.CharField(max_length=250)),
                ("unitofmeasurement", models.CharField(max_length=250)),
                (
                    "MANUFACTUREID",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.manufacture",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Customerordersub",
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
                ("quantity", models.CharField(max_length=100)),
                (
                    "CUSTOMERORDERMAIN",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.customerordermain",
                    ),
                ),
                (
                    "MANUFACTUREPRODUCT",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.manufactureproducts",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Productordermain",
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
                ("orderdate", models.DateField()),
                ("orderstatus", models.CharField(max_length=100)),
                ("price", models.CharField(max_length=100)),
                (
                    "PRODUCTS",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.products"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Productsub",
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
                ("description", models.CharField(max_length=100)),
                ("quantity", models.CharField(max_length=100)),
                (
                    "PRODUCTSUBORDERMAIN",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.productordermain",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Purchasemain",
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
                ("manufacture", models.CharField(max_length=250)),
                (
                    "PRODUCT",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.manufacture",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Purchasesub",
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
                ("product", models.CharField(max_length=250)),
                ("quantity", models.CharField(max_length=100)),
                (
                    "PURCHASEMAIN",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.purchasemain",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rawmaterialordermain",
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
                ("date", models.DateField()),
                ("amount", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=100)),
                (
                    "MANUFACTURE",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.manufacture",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Rawmaterialoredrsub",
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
                ("productdescription", models.CharField(max_length=250)),
                ("quantity", models.CharField(max_length=100)),
                (
                    "RAWMATERIALORDERMAIN",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.rawmaterialordermain",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Seller",
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
                ("companyname", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("place", models.CharField(max_length=100)),
                ("post", models.CharField(max_length=100)),
                ("pin", models.IntegerField()),
                ("phone", models.BigIntegerField()),
                ("website", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("dateofbirth", models.DateField()),
                ("status", models.CharField(max_length=100)),
                ("certificate", models.CharField(max_length=250)),
                (
                    "LOGIN",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.login"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Stockrawmaterial",
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
                ("quantity", models.IntegerField()),
                (
                    "RAWMATERIAL",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.rawmaterials",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Supplier",
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
                ("companyname", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("phone", models.BigIntegerField()),
                ("website", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("industry", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=100)),
                ("logo", models.CharField(max_length=250)),
                ("certification", models.CharField(max_length=250)),
                (
                    "LOGIN",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.login"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="rawmaterials",
            name="SUPPLIER",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.supplier"
            ),
        ),
        migrations.CreateModel(
            name="User",
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
                ("username", models.CharField(max_length=100)),
                ("email", models.CharField(max_length=100)),
                ("place", models.CharField(max_length=100)),
                ("post", models.CharField(max_length=100)),
                ("pin", models.IntegerField()),
                ("district", models.CharField(max_length=100)),
                ("phone", models.BigIntegerField()),
                ("gender", models.CharField(max_length=100)),
                (
                    "LOGIN",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.login"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="purchasemain",
            name="SELLER",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.user"
            ),
        ),
        migrations.CreateModel(
            name="Payment",
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
                ("paymentdate", models.DateField()),
                ("paymentamount", models.CharField(max_length=100)),
                ("paymentstatus", models.CharField(max_length=100)),
                (
                    "ORDER",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapp.customerordermain",
                    ),
                ),
                (
                    "LOGIN",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
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
                ("date", models.DateField()),
                ("rating", models.CharField(max_length=100)),
                ("feedbacktype", models.CharField(max_length=100)),
                (
                    "USER",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.user"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="customerordermain",
            name="USER",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="myapp.user"
            ),
        ),
        migrations.CreateModel(
            name="Complaint",
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
                ("date", models.DateField()),
                ("complaint", models.CharField(max_length=100)),
                ("status", models.CharField(max_length=100)),
                ("reply", models.CharField(max_length=100)),
                (
                    "USER",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="myapp.user"
                    ),
                ),
            ],
        ),
    ]