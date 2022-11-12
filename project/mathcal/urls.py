from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.mathcal,name='mathcal page')
]
