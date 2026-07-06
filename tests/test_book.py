from lib.book import Book

def test_book_instantiates():
    book = Book("Title", "Author", 1, "image_url")
    
    assert book.id == 1
    assert book.title == "Title"
    assert book.author == "Author"
    assert book.image_url == "image_url"

def test_books_equal():
    book_1 = Book(1, "Title", "Author", "image_url")
    book_2 = Book(1, "Title", "Author", "image_url")

    assert book_1 == book_2

def test_book_formats_correct():
    book = Book("Title", "Author", 1, "image_url")

    assert str(book) == "Book(1, Title, Author, image_url)"