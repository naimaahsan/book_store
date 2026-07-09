from lib.book import Book

class BookRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM books ORDER by id'
        )
        books = []
        for row in rows:

            item = Book(row["title"], row["author"], row["id"], row["image_url"])
            books.append(item)

        return books 
    
    def create(self, book):
        self._connection.execute(
            'INSERT INTO books (title, author, image_url) VALUES (%s, %s, %s)', [book.title, book.author, book.image_url]
        )
        return None
    
    def delete(self, book_id):
        self._connection.execute(
            'DELETE FROM books WHERE id = %s', [book_id]
        )

        return None
