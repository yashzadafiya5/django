from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('',views.index,name='indexpage'),
    path('home',views.home,name='homepage'),
    path('support',views.support,name='supportpage'),
    path('millinum/<int:year>/',views.millinum,name='millinum year'),
    path('bignumber/<int:number1>/<int:number2>/',views.bignumber,name='millinum year'),
]
