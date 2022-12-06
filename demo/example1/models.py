from django.db import models

class demo(models.Model):
    dname=models.CharField(max_length=125)
    dadd=models.TextField(max_length=525)
    
