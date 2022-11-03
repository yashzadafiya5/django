from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('',views.index,name='indexpage'),
    path('home',views.home,name='homepage')
]
