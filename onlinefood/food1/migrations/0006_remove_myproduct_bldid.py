# Generated by Django 4.0.5 on 2022-12-17 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food1', '0005_rename_shopkeeperid_myproduct_sellprice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myproduct',
            name='bldid',
        ),
    ]