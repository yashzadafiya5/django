# Generated by Django 4.0.5 on 2022-11-17 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paymentid', models.IntegerField()),
                ('cname', models.CharField(max_length=50)),
                ('add', models.TextField(max_length=540)),
                ('email', models.CharField(max_length=150)),
            ],
        ),
    ]
