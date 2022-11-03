from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1> hello! this is index page <h1/>')

def home(request):
    return render(request,"new.html")
