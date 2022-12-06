from django.db import models

class category(models.Model):
    title=models.CharField(max_length=128)
    description=models.TextField(max_length=512)
    status=models.IntegerField(max_length=1,default=0,null=True)
    photo=models.ImageField(upload_to='pics')
