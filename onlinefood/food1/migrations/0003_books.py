# Generated by Django 4.0.5 on 2023-01-28 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food1', '0002_alter_mybill_pincode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
            ],
        ),
    ]