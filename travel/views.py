from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'travel/home.html')

def about(request):
    return render(request, 'travel/about.html')

