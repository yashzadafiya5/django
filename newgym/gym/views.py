from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"home.html")
def aboutus(request):
    return render(request,"aboutus.html")
def eqipments(request):
    return render(request,"eqipments.html")
def ourteam(request):
    return render(request,"ourteam.html")
def branches(request):
    return render(request,"branches.html")
def wokwithus(request):
    return render(request,"wokwithus.html")



