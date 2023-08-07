CREATE DATABASE movie_database;

\c movie_database postgres;

CREATE TABLE IF NOT EXISTS movies (
    id INT NOT NULL,
    title VARCHAR(50) NOT NULL
);

INSERT INTO movies
VALUES (1, 'Test Movie');