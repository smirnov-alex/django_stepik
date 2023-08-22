from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from .models import Movie, Director, Actor


# Create your views here.
def show_all_movies(request):
    movies = Movie.objects.order_by(F('year').asc(nulls_first=True), 'rating')
    # movies = Movie.objects.annotate(new_field_bool=Value(True),
    #                                false_bool=Value(False),
    #                                new_budget=F('budget')+1000,
    #                                ffff=F('rating')*1.5,
    #                                )
    agg = movies.aggregate(Avg("budget"), Max("rating"), Min("rating"), Count('name'))
    return render(request, 'movie_app/all_movies.html', {'movies': movies, 'agg': agg})


def show_one_movie(request, slug_movie:str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', {'movie': movie})


def show_all_directors(request):
    directors = Director.objects.all()
    return render(request, 'movie_app/all_directors.html', {'directors':directors})


def show_one_director(request, director_id: int):
    director = get_object_or_404(Director, id=director_id)
    return render(request, 'movie_app/one_director.html', {'director': director})


def show_all_actors(request):
    actors = Actor.objects.all()
    return render(request, 'movie_app/all_actors.html', {'actors': actors})


def show_one_actor(request, actor_id: int):
    actor = get_object_or_404(Actor, id=actor_id)
    return render(request, 'movie_app/one_actor.html', {'actor': actor})
