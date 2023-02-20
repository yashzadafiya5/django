from django.shortcuts import render
from django.http import HttpResponse
from .models import categorys, Products, User, Cart,Bill,City,Book
from .myform import RagisterForm as i
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
# Create your views here.


def index(request):
    table = Products.objects.order_by('-id')[0:10]
    # print(len(table))
    return render(request, 'index.html', {'table': table})


def product(request, cateid, categoryname):
    table = Products.objects.filter(categoryid=cateid)
    return render(request, 'product.html', {'table': table, 'categoryname': categoryname})


def product_detail(request):
    return render(request, 'product-detail.html')


def singleblog(request):
    return render(request, 'single-blog.html')


def singleproduct(request, productid):
    table = Products.objects.filter(id=productid)
    row = table[0]
    return render(request, 'single-product.html', {'row': row})


def tracking(request):
    return render(request, 'tracking.html')


def category(request):
    table = categorys.objects.all()
    return render(request, 'category.html', {'table': table})


def cheakout(request):
    return render(request, 'checkout.html')


def confirmation(request):
    return render(request, 'confirmation.html')


def contact(request):
    return render(request, 'contact.html')


def forgotpassword(request):
    return render(request, 'forgot_password.html')


def cart(request):
    sql = "select c.id 'id',c.quntity 'quntity',p.title 'title',p.price 'price',p.photo 'photo' from myproject_cart c ,myproject_products p where userid=%s and c.productid=p.id and billid=%s"
    table = Cart.objects.raw(sql, [request.session.get('userid'), 0])
    grand_total = 0
    for row in table:
        grand_total += row.price * row.quntity
    return render(request, 'cart.html', {'table': table, 'grand_total': grand_total})


def ad_to_cart(request,productid):
    userid = request.session.get('userid')
    Cart.objects.create(productid=productid,userid=userid, quntity=1, billid=0)
    return HttpResponse('done..........')


def login(request):
    return render(request, 'login2.html')


def register2(request):
    return render(request, 'register2.html')


def changepassword(request):
    return render(request, 'changepassword2.html')


def ok(request, email):
    table = User.objects.filter(email=email)
    return HttpResponse(len(table))


def verify_login(request):
    email = request.POST['loginemail']
    password = request.POST['loginpassword']
    table = User.objects.filter(email=email, password=password)
    size = len(table)
    if size == 1:
        for row in table:
            request.session['userid'] = row.id
            break
        return HttpResponse('1')
    else:
        return HttpResponse('0')


def add_user(request):
    email = request.POST['registeremail']
    mobile = request.POST['registermobile']
    password = request.POST['registerpassword']
    confirmpassword = request.POST['registerconfirmpassword']
    # if password==confirmpassword and User.objects.filter(email not in email).exists():
    #     User.objects.create(email=email,mobile=mobile,password=password)
    if User.objects.filter(email=email).exists():
        return HttpResponse('-1')
    else:
        if password == confirmpassword:
            User.objects.create(email=email, password=password, mobile=mobile)
            return HttpResponse('1')
        else:

            return HttpResponse('-1')


def delete_cart_items(request, cartid):
    Cart.objects.filter(id=cartid).delete()
    return HttpResponse('product is deleted')


def verify_placeorder(request):
    name = request.POST['fullname']
    mobile = request.POST['mobile']
    address = request.POST['address']
    state = request.POST['state']
    city = request.POST['city']
    pincode = request.POST['pincode']
    payment_mode = request.POST['payment_mode']
    print(name, address, state, city, pincode, mobile, payment_mode)
    # Bill.objects.create(name=name,address=address,state=state,city=city,pincode=pincode,mobile=mobile,productid=    )
    return HttpResponse('bill added')

def logout(request):
    del request.session['userid']
    return render(request,'login2.html')

class BookApiView(APIView):
    serializer_class=BookSerializer
    def get(self,request):
        allbooks=Book.objects.all().values()
        return Response({"Message":"List Of Books","Book List":allbooks})
    
    def post(self,request):
        print("Request data is :",request.data)
        serializers_obj=BookSerializer(data=request.data)
        if (serializers_obj.is_valid()):
            Book.objects.create(id=serializers_obj.data.get('id'),
                                title=serializers_obj.data.get('title'),
                                author=serializers_obj.data.get('author'))
        
        book=Book.objects.all().filter(id=request.data['id']).values()
        return Response({"Message":"New Book Added.....","Book":book})