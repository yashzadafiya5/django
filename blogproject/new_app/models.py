from django.db import models

# Create your models here.

class Blog(models.Model):
    title=models.TextField(max_length=200)
    name=models.CharField(max_length=120)
    date=models.DateField(auto_now_add=True,null=True,blank=True)
    description=models.TextField(max_length=400)
    image=models.ImageField(upload_to='pics')
    
    def __str__(self):
        return self.title
    
