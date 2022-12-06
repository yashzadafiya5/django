from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def aboutus(request):
    return render(request,'aboutus.html')

def products(request):
    return render(request,'products.html')

def services(request):
    return render(request,'services.html')

def contactus(request):
    return render(request,'contactus.html')

def privacypolicy(request):
    return render(request,'privacypolicy.html')

def termsandconditions(request):
    return render(request,'termsandconditions.html')

def variables(request):
    return render(request,'variables.html')

def ifdemo(request,number):
    reminder = number%2
    return render(request,'if.html',{'number':number,'reminder':reminder})