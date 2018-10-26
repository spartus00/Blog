from django.urls import path
from . import views

urlpatterns = [
    path('travel/', views.home, name='travel-home'),
    path('travel/about', views.about, name='travel-about')
]