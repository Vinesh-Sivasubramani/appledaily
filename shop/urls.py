from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.collection,name='home'),
    path('about/',views.about,name='about'),
    path('blogs/<str:pk>',views.blog,name='blog')    
]