# Generated by Django 4.0.5 on 2022-11-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydatabase', '0003_delete_mymodel_delete_timestampedmodel_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ragister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField(max_length=128)),
                ('password', models.TextField(max_length=255)),
                ('mobile', models.TextField(max_length=16)),
                ('register_at', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]