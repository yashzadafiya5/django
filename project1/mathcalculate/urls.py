from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.home,name='home page'),
    path('getinput',views.getinput,name='home page'),
    path('getresult',views.getresult,name='result page'),
]
