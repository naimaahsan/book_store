# in a new file called `test_create_new_book.py`

from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection

def test_create_new_book(page: Page):
    connection = DatabaseConnection()
    connection.connect()

    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_label("Username").fill("test")
    page.get_by_label("Password").fill("1234")
    page.get_by_role("button", name="Login").click()

    page.goto("http://localhost:5001/books")
    page.get_by_placeholder("Title").fill("The BFG")
    page.get_by_placeholder("Author").fill("Roahl Dahl")
    page.get_by_role("button", name="Submit").click()
    books = page.locator(".book-thumbnail")

    books.first.wait_for(state="visible")
    
    new_book = books.all_inner_texts()[-1]
    assert new_book == "The BFG\n\nBy Roahl Dahl"

def test_create_new_book_unauth(page: Page):
    connection = DatabaseConnection()
    connection.connect()

    page.goto("http://localhost:5001/books")
    page.get_by_placeholder("Title").fill("The BFG")
    page.get_by_placeholder("Author").fill("Roahl Dahl")
    page.get_by_role("button", name="Submit").click()
    assert page.url == "http://localhost:5001/sessions/new"