# Generated by Django 4.0.5 on 2023-01-02 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0005_rename_product_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.IntegerField()),
                ('userid', models.IntegerField()),
                ('quntity', models.IntegerField()),
                ('billid', models.IntegerField()),
            ],
        ),
    ]
