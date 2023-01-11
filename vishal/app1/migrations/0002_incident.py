# Generated by Django 4.0.5 on 2023-01-04 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField(max_length=125)),
                ('department', models.TextField(max_length=250)),
                ('datetime', models.DateTimeField(auto_now_add=True, null=True)),
                ('incidentlocation', models.TextField(max_length=125)),
                ('inciseverity', models.TextField(max_length=125)),
                ('suspectcause', models.TextField(max_length=125)),
                ('immediattaken', models.TextField(max_length=125)),
                ('subincident', models.TextField(max_length=125)),
                ('repotedby', models.TextField(max_length=125)),
            ],
        ),
    ]
