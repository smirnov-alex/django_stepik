from django.shortcuts import render, get_object_or_404
from .models import Book


def show_all_books(request):
    books = Book.objects.order_by('title')
    return render(request, 'book_app/all_books.html', {'books': books})


def show_one_book(request, slug_book):
    book = get_object_or_404(Book, slug=slug_book)
    return render(request, 'book_app/book_detail.html', {'book': book})

