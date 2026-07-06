from lib.film import Film

def test_instantiates():
    film = Film("Film", "Genre", 1)
    assert film.id == 1
    assert film.title == "Film"
    assert film.genre =="Genre"

def test_films_equal():
    film_1 = Film("Film", "Genre", 1)
    film_2 = Film("Film", "Genre", 1)
    assert film_1 == film_2

def test_formats_correctly():
    film = Film("Film", "Genre", 1)
    assert str(film) == "Film(1, Film, Genre)"