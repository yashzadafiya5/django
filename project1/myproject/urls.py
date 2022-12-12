from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index page'),
    path('index',views.index,name='index page'),
    path('product/<int:cateid>/<str:categoryname>',views.product,name='product page'),
    path('product',views.product,name='product page'),
    path('product_detail',views.product_detail,name='product detail page'),
    path('register',views.register,name='register page'),
    path('singleblog',views.singleblog,name='product page'),
    path('singleproduct',views.singleproduct,name='product page'),
    path('tracking',views.tracking,name='product page'),
    path('category',views.category,name='category page'),
    path('cheakout',views.cheakout,name='cheakout page'),
    path('confirmation',views.confirmation,name='confirmation page'),
    path('contact',views.contact,name='contact page'),
    path('forgotpassword',views.forgotpassword,name='forgotpassword page'),
    path('cart',views.cart,name='cart page'),
    path('login',views.login,name='login page'),
    path('register2',views.register2,name='register2 page'),
    path('changepassword',views.changepassword,name='changepassword page'),
]
