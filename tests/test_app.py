import sys
import os
from playwright.sync_api import Page, expect
from lib.database_connection import DatabaseConnection

# this line is a bit of a hack which allows us to import app without changing anything else
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

# a descriptive test name
def test_get_books_returns_a_200():
    # here's where we make the test client
    client = app.test_client()

    # here's where we make the request
    response = client.get("/books")

    # here's where we assert that the response's status code is 200
    assert response.status_code == 200


def test_get_list_of_books(page: Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/books.sql")
    page.goto("http://127.0.0.1:5001/books")

    # 2. Target the actual container class instead of "li"
    books = page.locator(".caption")

    # 3. Update expectations to match the HTML structure (note the \n and capitalization)
    expected_books = [
        "The Gruffalo\n\nBy Julia Donaldson",
        "Ada Twist, Scientist\n\nBy Andrea Beaty",
        "The Girl Who Drank the Moon\n\nBy Kelly Barnhill",
        "Dragons in a Bag\n\nBy Zetta Elliott"
    ]

    # 4. Extract and assert
    actual_books = books.all_inner_texts()
    assert actual_books == expected_books

def test_get_list_of_films(page:Page):
    connection = DatabaseConnection()
    connection.connect()
    connection.seed("./seeds/films.sql")
    page.goto("http://127.0.0.1:5001/films")
    films = page.locator(".films")

    expected_films = [
        "Avatar\n\nGenre: Sci-Fi",
        "Titanic\n\nGenre: Romance",
        "Jurassic Park\n\nGenre: Adventure",
        "Frozen\n\nGenre: Animation",
        "The Dark Knight Rises\n\nGenre: Action"
    ]

    actual_films = films.all_inner_texts()
    assert actual_films == expected_films