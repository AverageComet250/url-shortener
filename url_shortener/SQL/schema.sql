DROP TABLE IF EXISTS links;

CREATE TABLE links (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    original TEXT NOT NULL,
    short TEXT NOT NULL
);