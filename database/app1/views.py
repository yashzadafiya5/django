from django.shortcuts import render
from django.http import HttpResponse
from .forms import RagisterForm,loginform,Myincident
from .models import ragister
# Create your views here.

def registerform(request):
    if request.method=='POST':
        forms=loginform()
        form=RagisterForm(request.POST)
        form.save()
        return render(request,'login.html',{'myform':forms})
    else:  
        form=RagisterForm()        
        return render(request,'register.html',{'form':form})
    
def login(request):
    if request.method=='POST':
        table=ragister.objects.filter(email=request.POST['email'],password=request.POST['password'])
        if table.count()==0:
            form=loginform()
            return render(request,'login.html',{'myform':form,'message':'invalid input'})
        else:
            request.session['id']=table.first().id 
            return render(request,'index.html')
    else:
        form=loginform()
        return render(request,'login.html',{'myform':form})

def verify_login(request):
    email=request.POST['email']
    password=request.POST['password']
    print(email,password)
    return HttpResponse('1')
    
def home(request):
    return render(request,'index.html')

def incident(request):
    if request.method=='POST':
        form=Myincident(request.POST)
        form.save()
        message='form saved successfully'
        return render(request,'incident.html',{'form':form,'message':message})
    else:
        form=Myincident()
        return render(request,'incident.html',{'form':form})
    
