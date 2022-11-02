import http
from django.shortcuts import render
from django.http import HttpResponse
from .models import Card

# from http import 

# Create your views here.

# def homePage(request):
#     # return HttpResponse("<h1>Namaskaram everyone</h1>")
#     render

# def aboutpage(request):
#     return HttpResponse("<h1>Welcome to about page</h1>")

# def services(request):
#     return HttpResponse("welcome to services")

# def contact(request):
#     return HttpResponse("contact")

def homePage(request):
    card = Card.objects.all()
    data = {
        'card':card
    }
    return render(request,'webpages/home.html',data)

def aboutpage(request):
    return render(request,'webpages/about.html')

def services(request):
    return render(request,'webpages/services.html')

def contact(request):
    return render(request, 'webpages/contact.html')