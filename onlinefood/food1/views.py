from django.shortcuts import render
from django.http import HttpResponse
from .models import Myshopkeper, Mybld, Mycategory, Myproduct, Mycart, Myuser, Mybill, Book
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
# Create your views here.


def divide_parts(list, size):
    for i in range(0, len(list), size):
        yield list[i:i+size]


def template(request):
    table = Myshopkeper.objects.all()
    return render(request, 'django_template.html', {'table': table})


def index(request):
    products = Myproduct.objects.order_by('-id')[0:10]
    hotels = Myshopkeper.objects.order_by('-id')[0:10]
    return render(request, 'index-2.html', {'products': products,'hotels':hotels})


def hotel(request):
    table = Myshopkeper.objects.all()
    return render(request, 'hotels.html', {'table': table})


def bld(request, hotelid):
    table = Mybld.objects.all().filter(shopkeperid=hotelid)
    return render(request, 'bld.html', {'table': table})


def category(request, blid):
    table = Mycategory.objects.all().filter(bldid=blid)
    return render(request, 'category.html', {'table': table})


def products(request, cateid):
    table = Myproduct.objects.all().filter(categoryid=cateid)
    return render(request, 'product.html', {'table': table})


def productdetail(request, prodid, cateid):
    table = Myproduct.objects.all().filter(id=prodid)
    table1 = Myproduct.objects.all().filter(categoryid=cateid)
    row = table[0]
    return render(request, 'productdetail.html', {'row': row, 'table1': table1})


def cart(request):
    userid = request.session['userid']
    sql = "select c.id 'id',c.quntity 'quntity',p.title 'title',p.sellprice 'price' from food1_mycart as c ,food1_myproduct as p where userid=%s and c.productid=p.id and billid=%s"
    table = Mycart.objects.raw(sql, [userid, 0])
    grand_total = 0
    for row in table:
        grand_total += row.quntity*row.price
    return render(request, 'cart.html', {'table': table, 'grand_total': grand_total})


def add_to_cart(request):
    userid = request.session['userid']
    productid = request.GET.get('productid')
    productprice = request.GET.get('productprice')
    Mycart.objects.create(
        productid=productid, price=productprice, quntity=1, billid=0, userid=userid)
    return HttpResponse("succfully worked.......")

def cart_delete(request,productid):
    Mycart.objects.filter(id=productid).delete()
    return HttpResponse('product delete successfully.....')

def checkout(request):
    userid = request.session['userid']
    sql = "select c.id 'id',c.quntity 'quntity',p.title 'title',p.sellprice 'price' from food1_mycart as c ,food1_myproduct as p where userid=%s and c.productid=p.id and billid=%s"
    table = Mycart.objects.raw(sql, [userid, 0])
    grand_total = 0
    for row in table:
        grand_total += row.quntity*row.price
    return render(request, 'checkout.html',{'table':table,'total':grand_total})


def verify_checkout(request):
    name = request.POST['name']
    address = request.POST['address']
    state = request.POST['state']
    city = request.POST['city']
    pincode = request.POST['pincode']
    mobile = request.POST['phonenumber']
    payment_mode = request.POST['payment_mode']

    sql = "select c.id,c.price 'price',c.quntity 'quntity',c.price 'price' from food1_mycart c where userid=%s"
    table = Mycart.objects.raw(sql, [request.session['userid']])
    grand_total = 0
    for row in table:
        quntity=row.quntity
        grand_total += row.price*quntity
    Mybill.objects.create(name=name,address=address,state=state,city=city,mobile=mobile,userid=request.session.get('userid'),quntity=quntity,payment_mode=payment_mode,pincode=pincode,total=grand_total)
    id=Mybill.objects.latest('id').id
    Mycart.objects.filter(billid=0,userid=request.session.get('userid')).update(billid=id)
    return HttpResponse('order will be successfully placeddddd........')

def login(request):
    return render(request, 'login2.html')


def verify_login(request):
    email = request.POST.get('login_email')
    password = request.POST.get('login_password')
    print(email, password)
    table = Myuser.objects.filter(email=email, password=password)
    if table.count() == 0:
        return HttpResponse('0')
    else:
        request.session['userid'] = table.first().id
        return HttpResponse('1')


def register(request):
    return render(request, 'register2.html')


def verify_register(request):
    name = request.POST.get('registername')
    email = request.POST.get('registeremail')
    password = request.POST.get('registerpassword')
    mobile = request.POST.get('registernumber')
    address = request.POST.get('registeraddress')
    city = request.POST.get('registercity')
    state = request.POST.get('registerstate')
    pincode = request.POST.get('registerpincode')
    table = Myuser.objects.filter(Q(email=email) | Q(mobile=mobile))
    size = len(table)
    if size >= 1:
        return HttpResponse('-1')
    else:
        Myuser.objects.create(name=name, email=email, password=password, mobile=mobile,
                              address=address, city=city, state=state, pincode=pincode)
        return HttpResponse('1')


def logout(request):
    del request.session['userid']
    return render(request, 'login2.html')


class BookApiView(APIView):
    serializer_class = Bookserializer

    def get(self, request):
        allbooks = Book.objects.all().values()
        return Response({"Message": "List Of Books", "Book List": allbooks})

    def post(self, request):
        print("Request data is :", request.data)
        serializers_obj = Bookserializer(data=request.data)
        if (serializers_obj.is_valid()):
            Book.objects.create(title=request.data['title'],
                                author=request.data['author'])
        print(request.data['id'])
        book = Book.objects.all().filter(id=request.data['id']).values()
        return Response({"Message": "New Book Added.....", "Book": book})
