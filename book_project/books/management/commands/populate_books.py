from django.core.management.base import BaseCommand
from books.models import Book
from datetime import datetime
import random

class Command(BaseCommand):
    help = 'Populate the database with 100 sample books'

    def handle(self, *args, **kwargs):
        genres = ['Fiction', 'Non-Fiction', 'Fantasy', 'Sci-Fi', 'Thriller', 'Mystery', 'Biography', 'Historical', 'Romance']
        authors = ['J.K. Rowling', 'George R. R. Martin', 'J.R.R. Tolkien', 'Agatha Christie', 'Isaac Asimov', 'Stephen King', 'Jane Austen', 'Mark Twain', 'Ernest Hemingway']

        for i in range(100):
            title = f"Book Title {i+1}"
            author = random.choice(authors)
            genre = random.choice(genres)
            publish_date = datetime(2025, 1, 1)  # You can randomize this date if needed
            description = f"Description for Book {i+1}"

            book = Book(
                title=title,
                author=author,
                genre=genre,
                publish_date=publish_date,
                description=description
            )
            book.save()

        self.stdout.write(self.style.SUCCESS("Successfully added 100 books"))
