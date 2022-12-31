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
    path('cart/<int:productdetailid>',views.cart,name='cart page'),
    path('cheakout/<int:productdetailid>/<int:total>',views.cheakout,name='checkout page'),
]
