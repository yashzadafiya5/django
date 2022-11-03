from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("this is home page.......")
def aboutus(request):
    return HttpResponse("this is aboutus page.......")
def eqipments(request):
    return HttpResponse("this is eqipments page.......")
def ourteam(request):
    return HttpResponse("this is ourteam page.......")
def branches(request):
    return HttpResponse("this is branches page.......")
def wokwithus(request):
    return HttpResponse("this is wokwithus page.......")



