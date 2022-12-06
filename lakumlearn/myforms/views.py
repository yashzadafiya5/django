from django.shortcuts import render
from django.http import HttpResponse
from .forms import Myform
# Create your views here.
def home(request):
    return render(request,'home.html')
def getform(request):
    return render(request,'getform.html')
def formapi(request):
    myform=Myform
    return render(request,'formapi.html',{'myform':myform})
def getresult(request):
    num1=int(request.GET['num1'])
    num2=int(request.GET['num2'])
    choices=int(request.GET['choices'])
    result=None
    if choices==1:
        message='Addition'
        result=num1+num2 
    elif choices==2:
        message='Multiplication'
        result=num1*num2
    elif choices==3:
        message='Substraction'
        result=num1-num2
    elif choices==4:
        message='Division'
        result=num1/num2 
    else:
        message='invalid input'
    return render(request,'getresult.html',{'result':result,'msg':message})