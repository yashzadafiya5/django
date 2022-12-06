from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home page'),
    path('aboutus',views.aboutus,name='aboutus page'),
    path('trydata',views.trydata,name='trydata page'),
    path('getinputform',views.getinputform,name='get inputform page'),
    path('formresult',views.formresult,name='Form result page'),
    path('postinputform',views.postinputform,name='post input page'),
    path('postresult',views.postresult,name='post result page'),
    path('formapi',views.formapi,name='formapi page'),
    path('formapi2',views.formapi2,name='formapi2 page'),
]
