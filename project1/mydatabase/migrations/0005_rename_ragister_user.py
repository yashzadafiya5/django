# Generated by Django 4.0.5 on 2022-11-25 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mydatabase', '0004_ragister_delete_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ragister',
            new_name='user',
        ),
    ]
