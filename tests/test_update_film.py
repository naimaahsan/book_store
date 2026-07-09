from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection

def test_update_exiting_book(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql")

    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('tester123456', '12345');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_label("Username").fill("tester123456")
    page.get_by_label("Password").fill("12345")
    page.get_by_role("button", name="Login").click()

    page.goto("http://localhost:5001/films")
    page.get_by_text("Update").first.click()
    page.locator("input[name='new title']").fill("The Avengers")
    page.get_by_role("button", name="Update").click()

    expect(page.locator(".films", has_text="Avatar")).not_to_be_visible()
    expect(page.locator(".films", has_text="The Avengers")).to_be_visible()
    expect(page.locator(".films", has_text="Genre: Sci-Fi")).to_be_visible()
    assert page.url == "http://localhost:5001/films"

def test_update_film_unauth(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql") 

    page.goto("http://localhost:5001/films")
    page.get_by_text("Update").first.click()
    assert page.url == "http://localhost:5001/sessions/new"


def test_add_then_update_book(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql")

    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('tester1237', '12345');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_label("Username").fill("tester1237")
    page.get_by_label("Password").fill("12345")
    page.get_by_role("button", name="Login").click()

    page.goto("http://localhost:5001/films")
    page.get_by_placeholder("Title").fill("Filmm")
    page.get_by_placeholder("Genre").fill("Genree")
    page.get_by_role("button", name="Submit").click()

    page.locator(".film-thumbnail", has_text="Filmm").get_by_role("button", name="Update").click()

    page.locator("input[name='new title']").fill("Updated Film")
    page.locator("input[name='new genre']").fill("Updated Genre")
    page.get_by_role("button", name="Update").click()

    expect(page.locator(".films", has_text="Filmm")).not_to_be_visible()
    expect(page.locator(".films", has_text="Updated Film")).to_be_visible()
    expect(page.locator(".films", has_text="Updated Genre")).to_be_visible()
    assert page.url == "http://localhost:5001/films"