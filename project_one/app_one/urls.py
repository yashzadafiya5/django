from django.urls import path
from . import views
urlpatterns = [
        path('', views.index, name='index'),
        path('aboutus', views.aboutus, name='About us'),
        path('contactus',views.contactus,name='Contact us'),
        path('first',views.first,name='first page'),
        path('support',views.support,name='support page'),
        path('branch/<str:address>/<str:city>/<int:pincode>',views.branch,name='support page')
    ]