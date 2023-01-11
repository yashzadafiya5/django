from http.client import HTTPResponse
from django.shortcuts import render
from .myform import Myform
# Create your views here.
def index(request):
    return HTTPResponse("home page")
def getinput(request):
    return render(request,"getinput.html")
def postinput(request):
    return render(request,"postinput.html")

def getresult(request):
    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    choice = int(request.GET['choice'])
    print(num1,num2,choice)
    result = None
    # process 
    if choice==1:
        result = num1 + num2 
    elif choice==2:
        result = num1 - num2
    elif choice==3:
        result = num1 * num2 
    elif choice==4:
        result = num1 / num2 
    return render(request,"getresult.html",{"answer":result})


def formapi(request):
    forms=Myform
    return render(request,'formapi.html',{'myform':forms})