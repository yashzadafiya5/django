# Generated by Django 4.0.5 on 2022-12-17 05:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('food1', '0003_mybld_discription'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycategory',
            name='discription',
            field=models.TextField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
