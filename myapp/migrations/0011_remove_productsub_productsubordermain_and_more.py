# Generated by Django 4.0.1 on 2024-04-15 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_remove_rawmaterialoredrsub_rawmaterial_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsub',
            name='PRODUCTSUBORDERMAIN',
        ),
        migrations.RemoveField(
            model_name='productsub',
            name='description',
        ),
        migrations.AddField(
            model_name='productsub',
            name='PRODUCTSUBORDERMAIN_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='myapp.productordermain'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productsub',
            name='PRODUCT_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productsub',
            name='quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sellerordermain',
            name='date',
            field=models.CharField(max_length=15),
        ),
    ]
