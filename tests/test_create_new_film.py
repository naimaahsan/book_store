from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection

def test_create_new_film(page: Page):
    connection = DatabaseConnection()
    connection.connect()

    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('testing', '12346');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_label("Username").fill("testing")
    page.get_by_label("Password").fill("12346")
    page.get_by_role("button", name="Login").click()

    page.goto("http://localhost:5001/films")
    page.get_by_placeholder("Title *").fill("New Film")
    page.get_by_placeholder("Genre *").fill("Action")
    page.get_by_role("button", name="Submit").click()
    films = page.locator(".films")
    new_film = films.all_inner_texts()[-1]
    assert new_film == "New Film\n\nGenre: Action"


def test_create_new_film_unauth(page: Page):
    connection = DatabaseConnection()
    connection.connect()

    page.goto("http://localhost:5001/films")
    page.get_by_placeholder("Title *").fill("Film")
    page.get_by_placeholder("Genre *").fill("Genre")
    page.get_by_role("button", name="Submit").click()
    films = page.locator(".films")
    
    assert page.url == "http://localhost:5001/sessions/new"