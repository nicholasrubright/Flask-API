-- CREATE DATABASE movie_matcher;

-- \c movie_matcher postgres;

-- CREATE TABLE IF NOT EXISTS MMSessions (
--     id INT NOT NULL,
--     code TEXT NOT NULL,
--     match BOOLEAN NOT NULL,
--     movie_match_id INT,

--     PRIMARY KEY (id)
-- );

-- INSERT INTO MMSessions
-- values (1, 'testcode', false, NULL);

CREATE DATABASE MovieDatabase;

\c MovieDatabase postgres;

CREATE TABLE IF NOT EXISTS Movies (
    id 
)