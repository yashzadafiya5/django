from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home page'),
    path('home',views.home,name='home page'),
    path('aboutus',views.aboutus,name='aboutus page'),
    path('gallery',views.gallery,name='gallary page'),
    path('vidos',views.vidos,name='vidos page'),
    path('contactus',views.contactus,name='contactus page')
]

