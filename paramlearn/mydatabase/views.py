from django.shortcuts import render
from django.http import HttpResponse
from .forms import RagisterForm,loginform,changepasswordform,forgotpasswordform
from .models import ragister
# Create your views here.

def home(request):
    return HttpResponse('this is home page')
def ragisterform(request):
    if request.method=='POST':
        forms=loginform()
        form=RagisterForm(request.POST)
        form.save()
        return render(request,'login.html',{'myform':forms})
    else:  
        form=RagisterForm()        
        return render(request,'ragister.html',{'form':form})
    
def login(request):
    if request.method=='POST':
        table=ragister.objects.filter(email=request.POST['email'],password=request.POST['password'])
        if table.count()==0:
            form=loginform()
            return render(request,'login.html',{'myform':form,'message':'invalid input'})
        else:
            request.session['id']=table.first().id 
            return render(request,'home.html')
    else:
        form=loginform()
        return render(request,'login.html',{'myform':form})
    
def changepassword(request):
    if request.method=='POST':
        table=ragister.objects.filter(id=request.session['id'],password=request.POST['password'])
        if table.count()== 0:
            form=changepasswordform()
            return render(request,'changepassword.html',{'myform':form,'message':'invalid input'})
        else:
            form=loginform()
            if (request.POST['newpassword']==request.POST['confirmnewpassword']):
                ragister.objects.filter(pk=request.session['id']).update(password=request.POST['newpassword'])
                return render(request,'login.html',{'myform':form})
            else:
                form=changepasswordform()
                return render(request,'changepassword.html',{'myform':form,'message':'new password and confirmpassword must be same input'})
    else:   
        form=changepasswordform()
        return render(request,'changepassword.html',{'myform':form})

   
def forgot(request):
    if request.method=="POST":
        table=ragister.objects.filter(email=request.POST['email'])
        if table.count()==0:
            form=forgotpasswordform
            return render(request,'forgotpassword.html',{'myform':form,'message':'invalid email address'})
        else:
            return HttpResponse('newpassword send you in few minutes wait......')
    else:
        form=forgotpasswordform
        return render(request,'forgotpassword.html',{'myform':form})