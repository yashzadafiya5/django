from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.home,name='homepage'),
    path('home',views.home,name='homepage'),
    path('ragister',views.ragisterform,name='ragisterform'),
    path('login',views.login,name='loginform'),
    path('changepassword',views.changepassword,name='changepassword form'),
    path('forgot',views.forgot,name='forgotpassword form'),
]
