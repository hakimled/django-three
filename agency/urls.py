from django.urls import path
from . import views

urlpatterns = [
    path('mak/', views.agency , name='agency'),
    
    
]