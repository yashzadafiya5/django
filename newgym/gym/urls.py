from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home page'),
    path('aboutus',views.aboutus,name='aboutus page'),
    path('eqipments',views.eqipments,name='eqipments page'),
    path('ourteam',views.ourteam,name='ourteam page'),
    path('branches',views.branches,name='branches page'),
    path('wokwithus',views.wokwithus,name='wokwithus page'),
]


