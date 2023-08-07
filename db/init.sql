CREATE DATABASE MovieDatabase;

\c MovieDatabase postgres;

CREATE TABLE IF NOT EXISTS Movies (
    id INT NOT NULL,
    title VARCHAR(50) NOT NULL
);

INSERT INTO Movies
VALUES (1, 'Test Movie');