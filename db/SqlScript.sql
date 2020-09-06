CREATE TABLE users (
    UserID integer NOT NULL UNIQUE,
    UserName text NOT NULL,
    Password text NOT NULL,
    Role text NOT NULL
)
