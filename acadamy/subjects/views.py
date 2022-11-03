from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requests):
    return HttpResponse("this is home page")
def first(request):
    return render(request,"first.html")