# Generated by Django 4.0.5 on 2022-12-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food1', '0004_mycategory_discription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myproduct',
            old_name='shopkeeperid',
            new_name='sellprice',
        ),
        migrations.RemoveField(
            model_name='myproduct',
            name='bld',
        ),
        migrations.AlterField(
            model_name='myproduct',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='myproduct',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
