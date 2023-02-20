from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def blog(request):
    table=Blog.objects.all()
    return render(request,'blog.html',{'table':table})

def blog_detail(request):
    return render(request,'blog_detail.html')

def About_Us(request):
    return render(request,'about_us.html')

# def handle_not_found(request,exception):
# 	return render(request,'handle_not_found.html')