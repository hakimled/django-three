from django.urls import path
from . import views




# app_name = 'news'

urlpatterns = [
    path('', views.news , name='news'),
    path('<int:cat_id>/' ,  views.category , name='category'),
    path('<str:wil_id>/' , views.wildetail, name='wilaya'),
    path('follow/follow/' , views.following, name='follow'),
    path('dests/dest/' , views.dest, name='destination'),
    # path('', views.CategoryView.as_view(), name='news'),
]
