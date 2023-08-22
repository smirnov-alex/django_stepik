from django.urls import path
from . import views

urlpatterns = [
    path('directors/<int:director_id>', views.show_one_director, name='director_detail'),
    path('actors/<int:actor_id>', views.show_one_actor, name='actor_detail'),
    path('directors/', views.show_all_directors, name='all_directors'),
    path('actors/', views.show_all_actors, name='all_actors'),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie_detail'),
    path('', views.show_all_movies, name='all_movies'),
]
