from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.index,name='index page'),
    path('index',views.index,name='index page'),
    path('template',views.template,name='template page'),
    path('hotel',views.hotel,name='hotel page'),
    path('bld/<int:hotelid>',views.bld,name='bld page'),
    path('category/<int:blid>',views.category,name='category page'),
    path('products/<int:cateid>',views.products,name='product page'),
    path('productdetail/<int:prodid>/<int:cateid>',views.productdetail,name='productdetail page'),
    path('cart',views.cart,name='cart page'),
    path('add_to_cart',views.add_to_cart,name='add to cart page'),
    path('checkout',views.checkout,name='checkout page'),
    path('verify_checkout',views.verify_checkout,name='verify checkout page'),
    path('login',views.login,name='login page'),
    path('verify_login',views.verify_login,name='verify login page'),
    path('register',views.register,name='register page'),
    path('verify_register',views.verify_register,name='verify register page'),
    path('logout',views.logout,name='logout page'),
    path('cart_delete/<str:productid>',views.cart_delete,name='delete cart page'),
]
