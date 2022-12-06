from django.urls import path
from . import views
urlpatterns = [
        path('', views.index, name='index'),
        path('aboutus', views.aboutus, name='about us'),
        path('products', views.products, name='Products'),
        path('services', views.services, name='Services'),
        path('contactus', views.contactus, name='Contact us'),
        path('privacypolicy', views.privacypolicy, name='Privacy policy'),
        path('termsandconditions', views.termsandconditions, name='Term & conditions'),
        path('variables', views.variables, name='variables'),
        path('if/<int:number>', views.ifdemo, name='if'),
    ]