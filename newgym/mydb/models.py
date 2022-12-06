from django.db import models as m

class payment(m.Model):
    paymentid=m.IntegerField()
    cname=m.CharField(max_length=50)
    add=m.TextField(max_length=540)
    email=m.CharField(max_length=150)