from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1> hello! this is index page <h1/>')

def home(request):
    return render(request,"new.html")
def support(request):
    return render(request,"support.html",{'name':'param'})
def millinum(request,year):
    proce=year%1000
    return render(request,'millinumyear.html',{
        'year':year,
        'proce':proce,
    })
    
def bignumber(request,number1,number2):
    number=[]
    if number1>number2:
        number.append(f"number 1 is big :{number1}")
    else:
        # number=print(f"number 2 is big : {number2}")
        number.append(f"number 2 is big :{number2}")
    
    return render(request,'bignumber.html',{'number':number,
                                            })