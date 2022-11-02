from turtle import home
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.homePage,name='home'),
    path('about',views.aboutpage,name='about'),
    path('services',views.services,name='services'),
    path('contact',views.contact,name='contact')
]