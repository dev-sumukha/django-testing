from django.shortcuts import render,HttpResponse

# Create your views here.
def homePage2(request):
    return HttpResponse("<h1>Hi</h1>")