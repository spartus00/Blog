from django.urls import path
from . import views

urlpatterns = [
    path('checklist/', views.home, name='checklist-home'),
]