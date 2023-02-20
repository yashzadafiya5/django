from django.db import models

class MyAdmin(models.Model):
    usename=models.TextField(max_length=124)
    password=models.TextField(max_length=124)
    
class Myshopkeper(models.Model):
    name=models.TextField(max_length=124)
    email=models.CharField(max_length=60)
    password=models.TextField(max_length=50)
    compneyname=models.CharField(max_length=50)
    address=models.TextField(max_length=200)
    state=models.TextField(max_length=40)
    city=models.TextField(max_length=40)
    pincode=models.TextField(max_length=20)
    mobile=models.CharField(max_length=20)
    discription=models.CharField(max_length=124)
    image=models.ImageField(upload_to='pics')
    isdeleted=models.IntegerField(default=0,null=True)
    
    def __str__(self):
        return (self.name)
    
class Mybld(models.Model):
    shopkeperid=models.IntegerField()
    title=models.TextField(max_length=128)
    image=models.ImageField(upload_to='pics')
    discription=models.TextField(max_length=200)
    isdeleted=models.IntegerField(default=0,null=True)

    def __str__(self) :
        return (self.title)
    
class Mycategory(models.Model):
    bldid=models.IntegerField()
    title=models.TextField(max_length=128)
    image=models.ImageField(upload_to='pics')
    discription=models.TextField(max_length=200)
    isdeleted=models.IntegerField(default=0,null=True)
    
class Myproduct(models.Model):
    title=models.TextField(max_length=124)
    price=models.IntegerField()
    sellprice=models.IntegerField()
    description=models.TextField(max_length=220)
    categoryid=models.IntegerField()
    image=models.ImageField(upload_to='pics')
    stock=models.IntegerField()
    isdeleted=models.IntegerField(default=0 ,blank=True,null=True)
    
   
class Myuser(models.Model):
    name=models.CharField(max_length=128)
    email=models.CharField(max_length=60)
    password=models.TextField(max_length=50)
    mobile=models.CharField(max_length=20)
    address=models.TextField(max_length=200)
    city=models.TextField(max_length=40)
    state=models.TextField(max_length=40)
    pincode=models.TextField(max_length=20)
    

   
class Mybill(models.Model):
    name=models.TextField(max_length=124)
    address=models.TextField(max_length=200)
    state=models.TextField(max_length=40)
    city=models.TextField(max_length=40)
    pincode=models.TextField(max_length=20)
    mobile=models.CharField(max_length=20)
    userid=models.IntegerField()
    quntity=models.IntegerField()
    payment_mode=models.IntegerField()
    total=models.IntegerField()
    billdate=models.DateField(auto_now_add=True,null=True,blank=True)
  
class Mycart(models.Model):
    productid=models.IntegerField()
    price=models.IntegerField()
    quntity=models.IntegerField()
    billid=models.IntegerField()
    userid=models.IntegerField()
    

class Book(models.Model):
    title=models.TextField(max_length=200)
    author=models.TextField(max_length=200)