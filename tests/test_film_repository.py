from lib.film_repository import FilmRepository
from lib.film import Film

def test_all_films(db_connection):
    db_connection.seed("seeds/films.sql")
    repository = FilmRepository(db_connection)
    films = repository.all()

    assert films == [
        Film('Avatar', 'Sci-Fi', 1, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRf_21ac3w7tjl0d1mjn9jOArW9SzBbS3vp6l97gDVgkQ&s=10)'),
        Film('Titanic', 'Romance', 2, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRErvzi-28e-p5B_jrBUhoStBmYgUg2OliDZzZ8BmC_yA&s=10)'),
        Film('Jurassic Park', 'Adventure', 3, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTYkQmIeKnp-g4ZR9lqaEq2uUGCi8Y3T-ohQFhbqaEYJw&s=10)'),
        Film('Frozen', 'Animation', 4, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh345oRxXqgUIHRC4Adai667S_SwMxArM4DNatiH4nXw&s=10)'),
        Film('The Dark Knight Rises', 'Action', 5, 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRR4NSVHDh0ozje-TkC0nTUssxXAfdicoxIC-Xe1PUhYw&s=10)')
    ]
