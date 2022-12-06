from django.db import models
import django
import datetime
from django_add_default_value import AddDefaultValue
class Category(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    status = models.IntegerField(max_length=1,null=True,default=0)
    photo = models.ImageField(upload_to='pics')
class Product(models.Model):
    categoryid = models.IntegerField()
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    price = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='pics')
class user(models.Model):
    email = models.TextField(max_length=128)
    password = models.TextField(max_length=255)
    mobile = models.TextField(max_length=16)
    register_at = models.DateField(auto_now_add=True, blank=True,null=True)

