from django.shortcuts import render
from django.http import HttpResponse
from .myform import Myform,MyBsform
# Create your views here.

def home(request):
    return render(request,'home.html')
def aboutus(request):
    return HttpResponse('<h1>this is about page</h1>')

def trydata(request):
    return render(request,'try.html')

def getinputform(request):
    return render(request,'forminput.html')

def formresult(request):
    num1=int(request.GET['num1'])
    num2=int(request.GET['num2'])
    choice=int(request.GET['choice'])
    print(num1,num2,choice)
    reault=None
    msg=''
    if choice==1:
        msg='Addition'
        result=num1+num2
    elif choice==2:
        msg='Substraction'
        result=num1-num2
    elif choice==3:
        msg='Multiplication'
        result=num1*num2
    elif choice==4:
        msg='Division'
        result=num1/num2
    return render(request,'formresult.html',{'result':result,'msg':msg})

def postinputform(request):
    return render(request,'postinput.html')
def postresult(request):
    return render(request,'postresult.html')

def formapi(request):
    myform=Myform
    return render(request,'formapi.html',{'myform':myform})
def formapi2(request):
    mybsform=MyBsform(request.POST)
    if mybsform.is_valid():
        print('this data is ok')    
    else:
        print('invalid input')
    return render(request,'formapi2.html',{'mybsform':mybsform})
