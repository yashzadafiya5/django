from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("hello this is index page...")
def product(request):
    return HttpResponse("this is product page")
def service(request):
    return HttpResponse("this is service page")
def blogs(request):
    return HttpResponse("this is blogs page")
def contactus(request):
    return HttpResponse("this is contactus page")


