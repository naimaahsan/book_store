import sys
import os

from app import app
from lib.database_connection import DatabaseConnection
from playwright.sync_api import Page

def test_auth_intergration():
    # create the test client to send requests without using Playwright and a browser
    client = app.test_client()

    # set up a DB connection
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) VALUES ('test', '1234');")

    # send the request
    response = client.post('/sessions', data={
        'username': 'test',
        'password': '1234'
    })

    # assert that the redirect happened
    assert response.status_code == 302

    # assert that the user was created
    assert response.headers['Location'].endswith('/books')

def test_auth_intergration_failed():
    # create the test client to send requests without using Playwright and a browser
    client = app.test_client()

    # set up a DB connection
    connection = DatabaseConnection()
    connection.connect()
    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) VALUES ('test', '1234');")

    # send the request
    response = client.post('/sessions', data={
        'username': 'test',
        'password': 'wong_password'
    })

    # assert that the redirect happened
    assert response.status_code == 302

    # assert that the user was created
    assert response.headers['Location'].endswith('/sessions/new')

def test_auth_playwright(page: Page):
    connection = DatabaseConnection()
    connection.connect()

    connection.execute("TRUNCATE TABLE users;")
    connection.execute("INSERT INTO users (username, password) values ('test', '1234');")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_label("Username").fill("test")
    page.get_by_label("Password").fill("1234")
    page.get_by_role("button", name="Login").click()

    assert page.url == "http://localhost:5001/books"


def test_auth_failed_playwright(page: Page):
    connection = DatabaseConnection()
    connection.connect()

    connection.execute("TRUNCATE TABLE users;")

    page.goto("http://localhost:5001/sessions/new")
    page.get_by_label("Username").fill("test")
    page.get_by_label("Password").fill("1234")
    page.get_by_role("button", name="Login").click()

    assert page.url == "http://localhost:5001/sessions/new"