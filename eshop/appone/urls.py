from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home page'),
    path('home',views.home,name='home page'),
    path('blogs',views.blogs,name='blog page'),
    path('contactus/<str:name>/<str:address>/<int:pincode>',views.contactus,name='contact us page'),
    path('product',views.product,name='product page'),
    path('service',views.service,name='service page'),
    path('if/<int:number>',views.demoif,name='if else page'),
]