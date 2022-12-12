# from django.db import models

# class Admin(models.Model):
#     usename=models.TextField(max_length=124)
#     password=models.TextField(max_length=124)
    
# class shopkeper(models.Model):
#     name=models.TextField(max_length=124)
#     email=models.CharField(max_length=60)
#     password=models.TextField(max_length=50)
#     compneyname=models.CharField(max_length=50)
#     address=models.TextField(max_length=200)
#     state=models.TextField(max_length=40)
#     city=models.TextField(max_length=40)
#     mobile=models.CharField(max_length=20)
#     discription=models.CharField(max_length=124)
#     image=models.ImageField(upload_to='pics')
#     isdeleted=models.IntegerField(default=0,null=True)
    
# class category(models.Model):
#     title=models.TextField(max_length=128)
#     image=models.ImageField(upload_to='pics')
#     shopkeperid=models.IntegerField()
#     isdeleted=models.IntegerField(default=0,null=True)

