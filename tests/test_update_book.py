from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection

def test_update_exiting_book(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")

    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('tester12345', '12345');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_label("Username").fill("tester12345")
    page.get_by_label("Password").fill("12345")
    page.get_by_role("button", name="Login").click()

    page.goto("http://localhost:5001/books")
    page.get_by_text("Update").first.click()
    page.locator("input[name='updated title']").fill("The Elephant")
    page.get_by_role("button", name="Update").click()

    expect(page.locator(".caption", has_text="The Gruffalo")).not_to_be_visible()
    expect(page.locator(".caption", has_text="The Elephant")).to_be_visible()
    expect(page.locator(".caption", has_text="By Julia Donaldson")).to_be_visible()
    assert page.url == "http://localhost:5001/books"

def test_update_book_unauth(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql") 

    page.goto("http://localhost:5001/books")
    page.get_by_text("Update").first.click()
    assert page.url == "http://localhost:5001/sessions/new"


def test_add_then_update_book(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")

    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('tester123', '12345');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_label("Username").fill("tester123")
    page.get_by_label("Password").fill("12345")
    page.get_by_role("button", name="Login").click()

    page.goto("http://localhost:5001/books")
    page.get_by_placeholder("Title").fill("A Book")
    page.get_by_placeholder("Author").fill("An Author")
    page.get_by_role("button", name="Submit").click()

    page.locator(".book-thumbnail", has_text="A Book").get_by_role("button", name="Update").click()

    page.locator("input[name='updated title']").fill("Updated Book")
    page.locator("input[name='updated author']").fill("Updated Author")
    page.get_by_role("button", name="Update").click()

    expect(page.locator(".caption", has_text="A Book")).not_to_be_visible()
    expect(page.locator(".caption", has_text="Updated Book")).to_be_visible()
    expect(page.locator(".caption", has_text="Updated Author")).to_be_visible()
    assert page.url == "http://localhost:5001/books"