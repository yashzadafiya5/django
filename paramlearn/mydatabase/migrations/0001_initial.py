# Generated by Django 4.0.5 on 2022-11-25 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ragister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=250)),
                ('mobile', models.CharField(max_length=20)),
            ],
        ),
    ]