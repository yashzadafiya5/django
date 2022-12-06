from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("this is my home page <hr/><a href='aboutus'>About us</a> <a href='contactus'>Contact us</a>")
def aboutus(request):
    return HttpResponse("this is about us page <hr/> <a href='contactus'>Contact us</a>")
def contactus(request):
    return HttpResponse("this is contact us page <hr/> <a href='aboutus'>About us</a>")
def first(request):
    return render(request,"first.html")
def support(request):
    return render(request,"support.html",
        {
        'address':'CG ROAD, Ahmedabad',
        'email':'support@gmail.com',
        'contact':'9876543210',
        })
def branch(request,address,city,pincode):
    return render(request,"branch.html",
    {
        'address':address,
        'city':city,
        'pincode':pincode,
    })