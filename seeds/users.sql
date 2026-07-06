DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

TRUNCATE table users;
-- Finally, we add any records that are needed for the tests to run

INSERT INTO users (username, password) VALUES 
('test_user', 'password123'),
('admin_user', 'secure_pass!');