from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def mathcal(request):
    return HttpResponse('this is mathcal page')
