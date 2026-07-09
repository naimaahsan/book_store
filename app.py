from flask import Flask, render_template, request, redirect, session
from lib.database_connection import DatabaseConnection
from lib.book_repository import BookRepository
from lib.book import Book
from lib.film_repository import FilmRepository
from lib.film import Film
from lib.user_repository import UserRepository
from lib.user import User
from lib.login_required import login_required

# instantiate a Flask app object
app = Flask(__name__)
app.secret_key = "some_really_secret_key" # adds encryption onto cache so cannot be hacked when making a session


# --- HOME ---

@app.route("/", methods=["GET"])
def index():
    return render_template("books/index.html")


# --- BOOKS ---

@app.route("/books", methods=["GET"])
def get_books():
    connection = DatabaseConnection()    # Initialize database connection tool
    connection.connect()   
    book_repository = BookRepository(connection)         # Pass the connection to the repository to allow SQL queries
    books = book_repository.all()                     # Run SELECT query and get list of Book objects
    return render_template("books/books.html", books=books) # Render books.html and inject the books data into the template

@app.route('/books', methods=["POST"])
@login_required
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book_details = request.form
    book = Book(title=book_details["title"], author=book_details["author"], image_url=book_details["image_url"])
    book_repository.create(book)
    return redirect("/books")

@app.route('/books/delete/<int:book_id>', methods=["POST"])
@login_required
def delete_book(book_id):
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book_repository.delete(book_id)
    return redirect('/books')

@app.route('/books/update/<int:book_id>', methods=["POST"])
@login_required
def save_updated_book(book_id):
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    title = request.form['updated title']
    author = request.form['updated author']
    image_url = request.form['updated image_url'] 
    updated_book = Book(title=title, author=author, image_url=image_url, id=book_id)
    book_repository.update(updated_book)
    return redirect('/books')

@app.route('/books/update/<int:book_id>', methods=["GET"])
@login_required
def show_update_page(book_id):
    connection = DatabaseConnection()
    connection.connect()
    book_repository = BookRepository(connection)
    book = book_repository.find(book_id)
    return render_template('books/update.html', book=book)
# --- FILMS ---

@app.route('/films', methods=["GET"])
def get_films():
    connection = DatabaseConnection()
    connection.connect()
    film_repostitory = FilmRepository(connection)
    films = film_repostitory.all()
    return render_template("films/films.html", films = films)

@app.route('/films', methods=["POST"])
@login_required
def create_film():
    connection = DatabaseConnection()
    connection.connect()
    film_repository = FilmRepository(connection)
    film_details = request.form 
    film = Film(title=film_details["title"], genre=film_details["genre"])
    film_repository.create(film)
    return redirect("/films")


# --- USERS: CREATE ---

@app.route('/users/new', methods=["GET"])
def sign_up_form():
    return render_template("users/signup_form.html")

@app.route('/users', methods=["POST"])
def create_user():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    user_details = request.form 
    user = User(username=user_details["username"], password=user_details["password"], id=None)
    user_repository.create(user)
    return redirect('/books')

# --- USERS: LOGIN ---

@app.route('/sessions/new', methods=["GET"])
def login_form():
    return render_template("users/login_form.html")

@app.route('/sessions', methods=["POST"])
def create_session():
    connection = DatabaseConnection()
    connection.connect()
    user_repository = UserRepository(connection)
    username = request.form["username"]
    password = request.form["password"]
    user = user_repository.find_by_username(username)

    if user and user.password == password:
        session["user_id"] = user.id
        session["username"] = user.username
        return redirect("/books")
    else:
        return redirect("/sessions/new")


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

