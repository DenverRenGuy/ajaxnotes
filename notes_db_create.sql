CREATE DATABASE notes;

USE notes;

CREATE TABLE notes(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    title VARCHAR(40) NOT NULL,
    description VARCHAR(255),
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
)
