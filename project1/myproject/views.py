from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def product(request):
    return render(request,'product.html')

def product_detail(request):
    return render(request,'product-detail.html')

def register(request):
    return render(request,'register.html')

def singleblog(request):
    return render(request,'single-blog.html')

def singleproduct(request):
    return render(request,'single-product.html')

def tracking(request):
    return render(request,'tracking.html')

def category(request):
    return render(request,'category.html')

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

def login(request):
    return render(request,'login2.html')