from flask import Flask, render_template, request, redirect
from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.book import Book
from lib.film_repository import FilmRepository
from lib.film import Film
from lib.user_repository import UserRepository
from lib.user import User

# instantiate a Flask app object
app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("books/index.html")

@app.route("/books", methods=["GET"])
def books():
    connection = DatabaseConnection()    # Initialize database connection tool
    connection.connect()   
    book_repository = BookRepository(connection)         # Pass the connection to the repository to allow SQL queries
    books = book_repository.all()                     # Run SELECT query and get list of Book objects
    return render_template("books/books.html", books=books) # Render books.html and inject the books data into the template

@app.route('/books', methods=["POST"])
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book_details = request.form
    book = Book(title=book_details["title"], author=book_details["author"], image_url=book_details["image_url"])
    book_repository.create(book)
    return redirect("/books")

@app.route('/films', methods=["GET"])
def films():
    connection = DatabaseConnection()
    connection.connect()
    film_repostitory = FilmRepository(connection)
    films = film_repostitory.all()
    return render_template("films/films.html", films = films)

@app.route('/users/new', methods=["GET"])
def sign_up_form():
    return render_template("users/signup_form.html")

@app.route('/users', methods=["POST"])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details = request.form 
    user = User(username=user_details["username"], password=user_details["password"])
    user_repository.create(user)
    return redirect('/books')

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

