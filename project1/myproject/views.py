from django.shortcuts import render
from django.http import HttpResponse
from .models import categorys,Products,User,Cart
from .myform import RagisterForm as i
from django.views.decorators.csrf import csrf_protect
# Create your views here.

def index(request):
    table=Products.objects.order_by('-id')[0:10]
    return render(request,'index.html',{'table':table})

def product(request,cateid,categoryname):
    table=Products.objects.all().filter(categoryid=cateid)
    return render(request,'product.html',{'table':table,'categoryname':categoryname})

def product_detail(request):
    return render(request,'product-detail.html')

def register(request):
    return render(request,'register.html')

def singleblog(request):
    return render(request,'single-blog.html')

def singleproduct(request,productid):
    table=Products.objects.all().filter(id=productid)
    row=table[0]
    return render(request,'single-product.html',{'row':row})

def tracking(request):
    return render(request,'tracking.html')

def category(request):
        table=categorys.objects.all()
        return render(request,'category.html',{'table':table})

def cheakout(request):
    return render(request,'checkout.html')

def confirmation(request):
    return render(request,'confirmation.html')

def contact(request):
    return render(request,'contact.html')

def forgotpassword(request):
    return render(request,'forgot_password.html')

def cart(request):
    return render(request,'cart.html')

def ad_to_cart(request):
    productid=request.GET.get('productid')
    Cart.objects.create(productid=productid,userid=-1,quntity=1,billid=0)
    return HttpResponse('done..........')

def login(request):
    return render(request,'login2.html')

def register2(request):
    return render(request,'register2.html')

def changepassword(request):
    return render(request,'changepassword2.html')


def ok(request,email):
    table=User.objects.all().filter(email=email)
    return HttpResponse(len(table))


def verify_login(request):
    email = request.POST['loginemail']
    password = request.POST['loginpassword']
    table=User.objects.all().filter(email=email,password=password)
    return HttpResponse(len(table))
