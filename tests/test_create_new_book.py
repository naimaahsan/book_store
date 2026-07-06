# in a new file called `test_create_new_book.py`

from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection

def test_create_new_book(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")
    page.goto("http://127.0.0.1:5001/books")
    page.get_by_placeholder("Title").fill("The BFG")
    page.get_by_placeholder("Author").fill("Roahl Dahl")
    page.get_by_role("button", name="Submit").click()
    books = page.locator(".book-thumbnail")
    new_book = books.all_inner_texts()[-1]
    assert new_book == "The BFG\n\nBy Roahl Dahl"
