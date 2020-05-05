CREATE_USERS = '''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        password VARCHAR(255)
    );
'''

CREATE_MOVIES = '''
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        rating REAL CHECK(rating > 0 and rating < 10)
    );
'''

CREATE_PROJECTION = '''
    CREATE TABLE IF NOT EXISTS projections(
        id INTEGER PRIMARY KEY,
        movie_id INTEGER,
        type VARCHAR(5),
        date VARCHAR(20),
        time VARCHAR(10),
        FOREIGN KEY(movie_id) REFERENCES movies(id)
    );
'''
CREATE_RESERVATION = '''
    CREATE TABLE IF NOT EXISTS reservations(
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        projection_id INTEGER,
        row INTEGER,
        col INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(projection_id) REFERENCES projection(id),
    );
'''

CREATE_SESSION = '''
    CREATE TEMP TABLE IF NOT EXISTS session(
        username VARCHAR(50)
    );
'''
