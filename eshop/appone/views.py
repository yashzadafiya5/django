from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("hello this is index page...")
def product(request):
    return HttpResponse("this is product page")
def service(request):
    return HttpResponse("this is service page")
def blogs(request):
    return HttpResponse("this is blogs page")
def contactus(request):
    return HttpResponse("this is contactus page")
def home(request):
    return render (request,'home.html',{'name':'param','address':'aksharvadi,bhavnager'})
def blogs(request):
    return render (request,'blogs.html',{'name':'param','address':'aksharvadi,bhavnager'})
def contactus(request,name,address,pincode):
    return render (request,'contactus.html',{
        'name':name,
        'address':address,
        'pincode':pincode,
        })
def product(request):
    return render (request,'product.html',{'name':'param','address':'aksharvadi,bhavnager'})
def service(request):
    return render (request,'service.html',{'name':'param','address':'aksharvadi,bhavnager'})

