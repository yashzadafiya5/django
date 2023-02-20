from django.urls import path 
from . import views 

urlpatterns = [
    path('home',views.home,name='home'),
    path('register',views.registerform,name='ragisterform'),
    path('login',views.login,name='loginform'),
    path('incident',views.incident,name='incident form'),
    path('verify_login',views.verify_login,name='verify login form'),
]
