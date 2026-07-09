from lib.film_repository import FilmRepository
from lib.film import Film

def test_all_films(db_connection):
    db_connection.seed("seeds/films.sql")
    repository = FilmRepository(db_connection)
    films = repository.all()

    assert films == [
        Film('Avatar', 'Sci-Fi', 1, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRM7DgT4oRUhxad_joaWTkQPmrttgcEs2yUAwZybkFKBQ&s=10'),
        Film('Titanic', 'Romance', 2, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnH7fCIsviy1SUp9eibv2XhADZXR2Oi9PfYqYowtJhnQ&s=10'),
        Film('Jurassic Park', 'Adventure', 3, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqe37l0ma2XnZSwn9UcW0WmZ6CSQJmJoaVMHeTBu8XeA&s=10'),
        Film('Frozen', 'Animation', 4, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh345oRxXqgUIHRC4Adai667S_SwMxArM4DNatiH4nXw&s=10)'),
        Film('The Dark Knight Rises', 'Action', 5, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRaZRYPjOrMkDMouLK0f6MvX2B6NHjv1frx_fjidpOYA&s=10')
    ]
