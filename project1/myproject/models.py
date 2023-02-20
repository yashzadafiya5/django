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
    
 
class Cart(models.Model):
    productid=models.IntegerField()
    userid=models.IntegerField()
    quntity=models.IntegerField()
    billid=models.IntegerField()
    
class Bill(models.Model):
    name=models.TextField(max_length=124)
    address=models.TextField(max_length=200)
    state=models.TextField(max_length=40)
    city=models.TextField(max_length=40)
    pincode=models.TextField(max_length=20)
    mobile=models.CharField(max_length=20)
    productid=models.IntegerField()
    userid=models.IntegerField()
    quntity=models.IntegerField()
    payment_mode=models.IntegerField()
    billdate=models.DateField(auto_now_add=True,null=True,blank=True)
    pincode=models.IntegerField()
    total=models.IntegerField()
    
    
class City(models.Model):
    cname=models.TextField(max_length=128)
    cpincode=models.IntegerField()
    
class Book(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.TextField(max_length=200)
    author=models.TextField(max_length=200)
    