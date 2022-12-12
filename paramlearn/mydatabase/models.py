from django.db import models

class ragister(models.Model):
    email=models.CharField(max_length=256)
    password=models.CharField(max_length=250)
    mobile=models.CharField(max_length=20)
    
    
