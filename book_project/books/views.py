from django.shortcuts import render
from .models import Book
from .forms import BookForm
from datetime import datetime

def book_list(request):
    # Default queryset
    books = Book.objects.all()
    
    # Handle filtering
    title_filter = request.GET.get('title')
    author_filter = request.GET.get('author')
    genre_filter = request.GET.get('genre')
    publish_date_filter = request.GET.get('publish_date')

    if title_filter:
        books = books.filter(title__icontains=title_filter)
    if author_filter:
        books = books.filter(author__icontains=author_filter)
    if genre_filter:
        books = books.filter(genre__icontains=genre_filter)
    if publish_date_filter:
        try:
            publish_date = datetime.strptime(publish_date_filter, "%Y-%m-%d")
            books = books.filter(publish_date=publish_date)
        except ValueError:
            pass  # If date is not valid, it will be ignored

    return render(request, 'books/book_list.html', {
        'books': books,
        'title_filter': title_filter,
        'author_filter': author_filter,
        'genre_filter': genre_filter,
        'publish_date_filter': publish_date_filter
    })


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookForm()

    return render(request, 'books/add_book.html', {'form': form})
