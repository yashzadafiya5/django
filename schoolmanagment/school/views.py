from django.http import HttpResponse
from django.shortcuts import render
import h11

# Create your views here.


def home(request):
  return render(request,'home.html')
def aboutus(request):
  return render(request,'aboutus.html')
def contactus(request):
  return render(request,'contactus.html',{'email':'email@gmail.com','mobile':'9857463214','Address':'aksharvadi','City':'bhavnager','Pincode':'364005'})
def gallery(request):
  return render(request,'gallery.html')
def videos(request):
  return render(request,'videos.html')
