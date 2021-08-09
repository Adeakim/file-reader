DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS books;
CREATE TABLE users (
        id BIGSERIAL PRIMARY KEY,
        username VARCHAR,
        first_name VARCHAR,
        last_name VARCHAR,
        created_at TIMESTAMP DEFAULT NOW(),
        uptime_at TIMESTAMP DEFAULT NOW()

    );


CREATE TABLE books (
        id BIGSERIAL PRIMARY KEY,
        user_id INTEGER,
        name VARCHAR,
        pages VARCHAR,
        created_at  TIMESTAMP DEFAULT NOW(),
        uptime_at  TIMESTAMP DEFAULT NOW(),
        CONSTRAINT fk_user
        FOREIGN KEY(user_id)
        REFERENCES users(id)
        ON DELETE CASCADE


    );

