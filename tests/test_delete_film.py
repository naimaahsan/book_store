from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection

def test_delete_exiting_film(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql") 

    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('testers', '12345');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_label("Username").fill("testers")
    page.get_by_label("Password").fill("12345")
    page.get_by_role("button", name="Login").click()

    page.goto("http://localhost:5001/films")

    page.on("dialog", lambda d: d.accept()) # Set up listener: "If a dialog pops up at any point in the future, catch it and click OK."
    page.get_by_text("Delete").first.click()
    
    films = page.locator(".films")
    assert films.count() == 4
    

def test_delete_film_unauth(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql") 

    page.goto("http://localhost:5001/books")
    page.on("dialog", lambda d: d.accept())
    page.get_by_text("Delete").first.click()
    assert page.url == "http://localhost:5001/sessions/new"


def test_add_then_delete_film(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql")

    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('testerss', '12345');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_label("Username").fill("testerss")
    page.get_by_label("Password").fill("12345")
    page.get_by_role("button", name="Login").click()

    page.goto("http://localhost:5001/films")
    page.get_by_placeholder("Title").fill("New Film")
    page.get_by_placeholder("Genre").fill("Test Genre")
    page.get_by_role("button", name="Submit").click()

    new_film = page.locator(".film-thumbnail", has_text="New Film")
    
    page.on("dialog", lambda d: d.accept())
    new_film.get_by_role("button", name="Delete").click()

    films = page.locator(".films")
    assert films.count() == 5