DROP TABLE IF EXISTS films;
DROP SEQUENCE IF EXISTS films_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS films_id_seq;
CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255)
);

TRUNCATE table films;
-- Finally, we add any records that are needed for the tests to run
INSERT INTO films (title, genre) VALUES 
('Avatar', 'Sci-Fi'),
('Titanic', 'Romance'),
('Jurassic Park', 'Adventure'),
('Frozen', 'Animation'),
('The Dark Knight Rises', 'Action');
