# Generated by Django 4.0.1 on 2024-04-15 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_remove_sellerordermain_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerordermain',
            name='SELLER',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.seller'),
        ),
    ]
