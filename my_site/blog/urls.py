from django.urls import path
from . import views

urlpatterns = [
    path('posts/keanu_reeves/', views.keanu_reeves),
    path('posts/guinness_world_records/', views.get_guinness_world_records),
    path('posts/<int:number_post>/', views.post_number),
    path('posts/<name_post>/', views.post_info),
    path('posts/', views.posts),
    path('people', views.people_detail),
    path('', views.index),
]
