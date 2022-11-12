from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('this is homepage')

def getinput(request):
    return render(request,'getinput.html')

def getresult(request):
    num1=int(request.GET['num1'])
    num2=int(request.GET['num2'])
    choice=int(request.GET['choice'])
    print(num1,num2,choice)
    result=None 
    results=[]
    if choice==1:
        result=num1+num2 
        results.append(f" Addition : {result}")
    elif choice==2:
        result=num1-num2 
        results.append(f" Substraction : {result}")
    elif choice==3:
        result=num1*num2 
        results.append(f" Multiplicaton : {result}")
    elif choice==4:
        result=num1/num2 
        results.append(f" Division : {result}")
    return render(request,'getresult.html',{
        'results':results,
    })

