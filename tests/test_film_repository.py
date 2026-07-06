from lib.film_repository import FilmRepository
from lib.film import Film

def test_all_films(db_connection):
    db_connection.seed("seeds/books.sql")
    repository = FilmRepository(db_connection)
    films = repository.all()

    assert films == [
        Film('Avatar', 'Sci-Fi', 1),
        Film('Titanic', 'Romance', 2),
        Film('Jurassic Park', 'Adventure', 3),
        Film('Frozen', 'Animation', 4),
        Film('The Dark Knight Rises', 'Action', 5)
    ]
