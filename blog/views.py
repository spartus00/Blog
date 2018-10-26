from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>About</h1>')

def travel(request):
    return HttpResponse('<h1>travel</h1>')