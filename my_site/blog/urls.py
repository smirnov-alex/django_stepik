from django.urls import path
from . import views

urlpatterns = [
    path('posts/<int:number_post>/', views.post_number),
    path('posts/<name_post>/', views.post_info),
    path('posts/', views.posts),
    path('', views.index),
]