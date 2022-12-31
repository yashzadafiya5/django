from django.shortcuts import render
from django.http import HttpResponse
from .models import Myshopkeper,Mybld,Mycategory,Myproduct,Mycart,Myuser,Mybill

# Create your views here.
def divide_parts(list,size):
    for i in range(0,len(list),size):
        yield list[i:i+size]
 
        
def template(request):
    table=Myshopkeper.objects.all()
    return render(request,'django_template.html',{'table':table})
        
def index(request):
    table1=Myproduct.objects.all().order_by('-id')[0:6]
    table=Mycategory.objects.all().order_by('-id')[0:6]
    table2=Myshopkeper.objects.all()
    table3=Myshopkeper.objects.all()
    table4=Mybill.objects.all()
    table5=Mybld.objects.filter(id=5)
    row=table[0]
    for row in table4:
        countfooddivery=Mybill.objects.all().count()
    for row in table3:
        counthotel=Myuser.objects.all().count()
    return render(request,'index-2.html',{'table':table,'table1':table1,'table2':table2,'counthotel':counthotel,'countfooddivery':countfooddivery,'row':row})

def hotel(request):
    table=Myshopkeper.objects.all()
    return render(request,'hotels.html',{'table':table})

def bld(request,hotelid):
    table=Mybld.objects.all().filter(shopkeperid=hotelid)
    return render(request,'bld.html',{'table':table})


def category(request,blid):
    table=Mycategory.objects.all().filter(bldid=blid)
    return render(request,'category.html',{'table':table})

def products(request,cateid):
    table=Myproduct.objects.all().filter(categoryid=cateid)
    return render(request,'product.html',{'table':table})

def productdetail(request,prodid,cateid):
    table=Myproduct.objects.all().filter(id=prodid)
    table1=Myproduct.objects.all().filter(categoryid=cateid)
    row=table[0]
    return render(request,'productdetail.html',{'row':row,'table1':table1})

def cart(request,productdetailid):
    table=Myproduct.objects.all().filter(id=productdetailid)
    for row in table:
        total = row.sellprice * row.stock
    return render(request,'cart.html',{'table':table,'total':total})

def cheakout(request,productdetailid,total):
    table=Myproduct.objects.all().filter(id=productdetailid)
    table1=Myuser.objects.all()
    row1=table1[0]
    row=table[0]
    return render(request,'checkout.html',{'row':row,'row1':row1,'total':total})

