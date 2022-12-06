from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='homepage'),
    path('aboutus',views.aboutus,name='aboutus page'),
    path('contactus/<str:name>/<int:age>/<str:add>',views.contactus,name='contactus page'),
    path('fillform',views.fillform,name='fillform page'),
    path('formresult',views.formresult,name='formresult page'),
    path('formapi',views.formapi,name='formapi page'),
]
