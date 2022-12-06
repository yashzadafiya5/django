from django.shortcuts import render
from django.http import HttpResponse
from .myform import RagisterForm,loginform,changepasswordform,forgetpasswordform
from .models import user
# Create your views here.

def index(request):
    return HttpResponse('this is index page')
def home(request):
    return render(request,'home.html')
def changepassword(request):
    if request.method=='POST':
        tabel=user.objects.filter(id=request.session['id'],password=request.POST['password'])
        if tabel.count()==0:
            form=changepasswordform()
            return render(request,'changepassword.html',{'form':form,'message':'invalid current password'})
        else:
            if request.POST['newpassword'] != request.POST['confiremnewpassword']:
                form=changepasswordform()
                return render(request,'changepassword.html',{'form':form,'message':'newpassword and confirm new password must be Same'})
            else:
                user.objects.filter(pk=request.session['id']).update(password=request.POST['newpassword'])
                form=loginform()
                return render(request,'login.html',{'form':form})
    else:   
        form=changepasswordform()
        return render(request,'changepassword.html',{'form':form})
def ragister(request):
    if request.method=='POST':
        form=loginform()
        myform=RagisterForm(request.POST)
        myform.save()
        return render(request,'login.html',{'form':form})
    else:
        form=RagisterForm()
        return render(request,'ragister.html',{'form':form})
    
def login(request):
    if request.method=='POST':
        form=loginform(request.POST)
        table=user.objects.filter(email=request.POST['email'],password=request.POST['password'])
        if table.count()==0:
            return render(request,'login.html',{'form':form,'message':'invalid Login Attempt'})
        else:
            request.session['id']=table.first().id
            return render(request,'home.html')
    else:
        form=loginform()
        return render(request,'login.html',{'form':form})
def forgetpassword(request):
    if request.method=='POST':
        table=user.objects.filter(email=request.POST['email'])
        if table.count()==0:
            form=forgetpasswordform(request.POST) 
            return render(request,'forgotpassword.html',{'form':form,'message':'email is invalid'})
        else:
            return HttpResponse('quickly new password gunrate and send on  your emailaddress')
    else:
        form=forgetpasswordform()
        return render(request,'forgotpassword.html',{'form':form})