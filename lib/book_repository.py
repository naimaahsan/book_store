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

            image_url = row.get("image_url") if "image_url" in row else None

            item = Book(row["id"], row["title"], row["author"], row["image_url"])
            books.append(item)

        return books 
