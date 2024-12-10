from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello! This is my first Website.")

def aboutpage(request):
    return render(request,'about.html')

def contactpage(request):
    return render(request,'contact.html')

