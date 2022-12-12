from django.db import models 

class categorys(models.Model):
    title=models.CharField(max_length=128)
    photo=models.ImageField(upload_to='pics')
    
class Products(models.Model):
    title=models.CharField(max_length=128)
    categoryid=models.IntegerField()
    photo=models.ImageField(upload_to='pics')
    price=models.IntegerField()
    stock=models.IntegerField()
    sellprice=models.IntegerField()
    description=models.TextField(max_length=128)
    
class User(models.Model):
    email=models.TextField(max_length=128)
    password=models.TextField(max_length=128)
    mobile=models.TextField(max_length=10)
    
