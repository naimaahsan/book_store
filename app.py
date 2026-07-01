from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository

# instantiate a Flask app object
app = Flask(__name__)
db = SQLAlchemy() # Initialize the SQLAlchemy ORM utility

# Database model that automatically maps this Python class to a SQL table
class ThumbnailItem(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Unique ID for each record; automatically increments
    title = db.Column(db.String(100), nullable=False) # Required string column for the book title (max 100 characters)
    author = db.Column(db.Text, nullable=True) # Optional text column for the author's name
    image_url = db.Column(db.String(255), nullable=False, default='default.jpg') # Required image link column; defaults to 'default.jpg' if left blank

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/books", methods=["GET"])
def books():
    connection = DatabaseConnection()    # Initialize database connection tool
    connection.connect()                 # Open active connection to the database
    book_repository = BookRepository(connection)         # Pass the connection to the repository to allow SQL queries
    db_books = book_repository.all()                     # Run SELECT query and get list of Book objects
    return render_template("books.html", books=db_books) # Render books.html and inject the db_books data into the template

# Declares a route that listens for a GET request to the path /hello
# and a method to execute when that request comes in

# @app.route('/hello', methods=['GET'])
# def hello():
#     return "Hello to you too"


# @app.route('/books', methods=['GET'])
# def get_books():
#     return [
#     {
#         "title": "The Gruffalo",
#         "author": "Julia Donaldson"
#     },
#     {
#         "title": "Ada Twist, Scientist",
#         "author": "Andrea Beaty"
#     },
#     {
#         "title": "The Girl Who Drank the Moon",
#         "author": "Kelly Barnhill"
#     },
#     {
#         "title": "Dragons in a Bag",
#         "author": "Zetta Elliott"
#     }
#     ]

# @app.route('/authors', methods=['GET'])
# def get_authors():
#     return [
#     {
#         "name": "Julia Donaldson",
#         "dob": "1948-09-16"
#     },
#     {
#         "name": "Andrea Beaty",
#         "dob": "1961-10-08"
#     },
#     {
#         "name": "Kelly Barnhill",
#         "dob": "1973-01-01"
#     },
#     {
#         "name": "Zetta Elliott",
#         "dob": "1979-11-11"
#     }
#     ]

# make the server run in response to `python app.py`
# on port 5001 (you'll learn more about what this means later)
# and use debug mode so that changing code restarts the app
if __name__ == "__main__":
    # app.run(port=5001, debug=True)
    app.run(host="0.0.0.0", port=5001, debug=True)

