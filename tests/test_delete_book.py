from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection

def test_delete_exiting_book(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql") 

    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('tester', '12345');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_label("Username").fill("tester")
    page.get_by_label("Password").fill("12345")
    page.get_by_role("button", name="Login").click()

    page.goto("http://localhost:5001/books")
    page.get_by_text("Delete").first.click()

    books = page.locator(".caption")
    assert books.count() == 3
    

def test_delete_book_unauth(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql") 

    page.goto("http://localhost:5001/books")
    page.get_by_text("Delete").first.click()
    assert page.url == "http://localhost:5001/sessions/new"


def test_add_then_delete_book(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")

    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('tester', '12345');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_label("Username").fill("tester")
    page.get_by_label("Password").fill("12345")
    page.get_by_role("button", name="Login").click()

    page.goto("http://localhost:5001/books")
    page.get_by_placeholder("Title").fill("New Book")
    page.get_by_placeholder("Author").fill("Test Author")
    page.get_by_role("button", name="Submit").click()

    new_book = page.locator(".book-thumbnail", has_text="New Book")
    
    new_book.get_by_role("button", name="Delete").click()

    books = page.locator(".caption")
    assert books.count() == 4