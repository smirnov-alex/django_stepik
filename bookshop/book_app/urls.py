from django.urls import path
from . import views

urlpatterns = [
    path('book/<str:slug_book>', views.show_one_book, name='book_detail'),
    path('', views.show_all_books),
]