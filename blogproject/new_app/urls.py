from django.urls import path 
from . import views 

urlpatterns = [
    path('blog',views.blog,name='blog page'),
    path('blog_detail/<int:blogid>',views.blog_detail,name='blog_detail page'),
    path('About_Us',views.About_Us,name='About_Us page'),
]
