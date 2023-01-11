from django.db import models

class ragister(models.Model):
    email=models.CharField(max_length=256)
    password=models.CharField(max_length=250)
    mobile=models.CharField(max_length=20)
    
class incident(models.Model):
    location=models.TextField(max_length=125)
    department=models.TextField(max_length=250)
    datetime=models.DateTimeField(auto_now_add=True ,blank=True,null=True)  
    incidentlocation=models.TextField(max_length=125)
    inciseverity=models.TextField(max_length=125)
    suspectcause=models.TextField(max_length=125)
    immediattaken=models.TextField(max_length=125)
    subincident=models.TextField(max_length=125)
    repotedby=models.TextField(max_length=125)
    
