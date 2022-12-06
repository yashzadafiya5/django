from django.shortcuts import render
from django.http import HttpResponse
from .myform import Myform,MyBsForm
# Create your views here.
def index(request):
    return render(request,'getform.html')

def getinput(request):
    return render(request,'getinput.html')

def getresult(request):
    number1=int(request.GET['num1'])
    number2=int(request.GET['num2'])
    choice=int(request.GET['choice'])
    result=None
    msg=''
    if choice==1:
        msg='addition'
        result=number1+number2
    elif choice==2:
        msg='Substraction'
        result=number1-number2
    elif choice==3:
        msg='Multiplication'
        result=number1*number2
    elif choice==4:
        msg='Division'
        result=number1/number2

    return render(request,'getresult.html',{
        'result':result,
        'message':msg
    })
    
def formapi(request):
    myform=Myform
    return render(request,'formapi.html',{
        'form':myform
    })
    
def postinput(request):
    return render(request,'postinput.html')

def formapi2(request):
    myform=MyBsForm 
    return render(request,'formapi2.html',{'myform2':myform})

def formapiresult(request):
    myform=MyBsForm(request.POST)
    if myform.is_valid():
        print('data is ok')
    else:
        print('invalid data')
    return HttpResponse('done')
    