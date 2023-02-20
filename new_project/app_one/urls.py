from django.urls import path 
from . import views 

urlpatterns = [
    path('index',views.index,name='index page'),
    path('add_user',views.add_user,name='add_user page'),
    path('edit_user/<str:userid>',views.edit_user,name='edit_user'),
    path('delete_user/<str:newuserid>',views.delete_user,name='delte page'),
    path('calender',views.calender,name='calender page'),
    
]
