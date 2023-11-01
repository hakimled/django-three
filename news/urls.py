from django.urls import path
from . import views


# app_name = 'news'

urlpatterns = [
    path('', views.news , name='news'),
    path('<int:pk>/' ,  views.category , name='category'),
]