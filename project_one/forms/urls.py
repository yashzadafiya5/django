from django.urls import path
from . import views
urlpatterns = [
        path('', views.index, name='index'),
        path('getinput',views.getinput, name='get input'),
        path('getresult',views.getresult, name='get result'),
        path('postinput',views.postinput, name='post input'),
        path('postresult',views.postresult, name='post result'),
        path('formapi',views.formapi, name='form api'),
    ]