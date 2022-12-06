from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.index,name='index page'),
    path('ragister',views.ragister,name='Ragister page'),
    path('login',views.login,name='login page'),
    path('home',views.home,name='home page'),
    path('changepassword',views.changepassword,name='changepassword page'),
    path('forgetpassword',views.forgetpassword,name='forgetpassword page'),
]
