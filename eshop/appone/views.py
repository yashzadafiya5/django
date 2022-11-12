from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request,'home.html',{'data':'20'
                                        })
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

def demoif(request,number):
    proc=number%2
    return render(request,'if.html',{
        'number':number,
        'proc':proc,
    })