from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.index,name='index page'),
    path('variable/<str:name>',views.variable,name='variable page'),
]
