from lib.book_repository import BookRepository
from lib.book import Book
from lib.database_connection import DatabaseConnection

def test_all_books(db_connection):
    db_connection.seed("seeds/books.sql")
    repository = BookRepository(db_connection)
    books = repository.all()

    assert books == [
        Book('The Gruffalo', 'Julia Donaldson', 1, 'https://voxblock.co.uk/cdn/shop/files/the-gruffalo-audiobook-character.webp?v=1714987686'),
        Book('Ada Twist, Scientist', 'Andrea Beaty', 2, 'https://m.media-amazon.com/images/I/81m0eJVO9vL._AC_UF894,1000_QL80_.jpg'),
        Book('The Girl Who Drank the Moon', 'Kelly Barnhill', 3, 'https://m.media-amazon.com/images/I/91bDYQ4S5WL._AC_UF894,1000_QL80_.jpg'),
        Book('Dragons in a Bag', 'Zetta Elliott', 4, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRvN310x7_U1b9twPx5SrU95sxENWyIQ4nlEY2HUlwQ1g&s=10')
    ]