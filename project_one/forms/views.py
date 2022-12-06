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
def postresult(request):
    #process 
    amount = str(request.POST['amount'])
    rate = str(request.POST['rate'])
    year =  str(request.POST['year'])
    abc=string.ascii_letters
    answer = ''
    msg = ""
    if amount.isdigit()==False or rate.isdigit()==False or year.isdigit()==False:
        msg='one or more input give'
    else:
        msg='Simple Intrest '
        amount = float(amount)
        rate = float(rate)
        year = float(year)
        answer = (amount * rate * year) / 100 
    return render(request,"postresult.html",{"result":answer,"message":msg})

def formapi(request):
    forms=Myform
    return render(request,'formapi.html',{'myform':forms})