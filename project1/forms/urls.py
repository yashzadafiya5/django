from django.urls import path 
from . import views 

urlpatterns = [
    path('',views.index,name='index page'),
    path('getinput',views.getinput,name='input page'),
    path('getresult',views.getresult,name='result page'),
    path('formapi',views.formapi,name='FormApi page'),
    path('formapi2',views.formapi2,name='FormApi2 page'),
    path('formapiresult',views.formapiresult,name='formapiresult page'),
]
