from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home page'),
    path('getform',views.getform,name='getform page'),
    path('getresult',views.getresult,name='getresult page'),
    path('formapi',views.formapi,name='formapi page'),
]
