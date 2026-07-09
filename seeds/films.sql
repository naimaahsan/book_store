DROP TABLE IF EXISTS films;
DROP SEQUENCE IF EXISTS films_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS films_id_seq;
CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    image_url TEXT
);

TRUNCATE table films;
-- Finally, we add any records that are needed for the tests to run
INSERT INTO films (title, genre, image_url) VALUES 
('Avatar', 'Sci-Fi', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRM7DgT4oRUhxad_joaWTkQPmrttgcEs2yUAwZybkFKBQ&s=10'),
('Titanic', 'Romance', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQnH7fCIsviy1SUp9eibv2XhADZXR2Oi9PfYqYowtJhnQ&s=10'),
('Jurassic Park', 'Adventure', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqe37l0ma2XnZSwn9UcW0WmZ6CSQJmJoaVMHeTBu8XeA&s=10'),
('Frozen', 'Animation', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh345oRxXqgUIHRC4Adai667S_SwMxArM4DNatiH4nXw&s=10)'),
('The Dark Knight Rises', 'Action', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRaZRYPjOrMkDMouLK0f6MvX2B6NHjv1frx_fjidpOYA&s=10');
