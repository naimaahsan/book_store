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
('Avatar', 'Sci-Fi', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-DLojKo3wqs8yTacNuM9-SRoq9kikRCKlWSHigdRkDw&s=10'),
('Titanic', 'Romance', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuIpILxfxzzRPddxcQJYvDsZoVPy4JW6ee4gL2Z9EUKA&s=10'),
('Jurassic Park', 'Adventure', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRH5kHgp-FzYkloVC41KyO8IXJMlDOrRImK_PunDQ-oJg&s=10)'),
('Frozen', 'Animation', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh345oRxXqgUIHRC4Adai667S_SwMxArM4DNatiH4nXw&s=10)'),
('The Dark Knight Rises', 'Action', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQq6_VhuC-AK-XpAWdL-6mMEt6hoVPilbU2aLRsicBXng&s=10');
