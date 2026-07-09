from lib.film import Film

class FilmRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM films ORDER by id'
        )
        films = []
        for row in rows:

            item = Film(row["title"], row["genre"], row["id"], row["image_url"])
            films.append(item)

        return films 
    
    def create(self, film):
        self._connection.execute(
            'INSERT INTO films (title, genre, image_url) VALUES (%s, %s, %s)', [film.title, film.genre, film.image_url]
        )
        return None
    
    def delete(self, film_id):
        self._connection.execute(
            'DELETE FROM films WHERE id = %s', [film_id]
        )

        return None

    def update(self, film):
        self._connection.execute(
            'UPDATE films SET title = %s, genre = %s, image_url = %s WHERE id = %s', [film.title, film.genre, film.image_url, film.id]
        )

        return None

    def find(self, film_id):
        rows = self._connection.execute(
            ' SELECT id, title, genre, image_url FROM films WHERE id = %s', [film_id]
        )

        row = rows[0]

        return Film(row["title"], row["genre"], row["id"], row["image_url"])