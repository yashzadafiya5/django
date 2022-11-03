from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home page'),
    path('product',views.product,name='product page'),
    path('service',views.service,name='service page'),
    path('blogs',views.blogs,name='blogs page'),
    path('contactus',views.contactus,name='contactus page'),
]


# product
# service
# blogs
# contactus