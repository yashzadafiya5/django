from django.shortcuts import render
from django.http import HttpResponse
from .myform import Myform
# Create your views here.
def home(request):
    return render(request,"index1.html")
def aboutus(request):
    return render(request,'index1.html')
def contactus(request,name,age,add):
    return render(request,'contactus.html',{'name':name,'age':age,'add':add,})
def fillform(request):
    return render(request,'form.html')
def formresult(request):
    num1=int(request.GET['num1'])
    num2=int(request.GET['num2'])
    choice=int(request.GET['choice'])
    print(num1,num2,choice)
    return render(request,'formresult.html')

def formapi(request):
    myform=Myform
    return render(request,'forminput.html',{'myform':myform})

