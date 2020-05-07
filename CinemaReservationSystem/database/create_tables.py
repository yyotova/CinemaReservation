CREATE_USERS = '''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        email VARCHAR(50) NOT NULL UNIQUE,
        password VARCHAR(255),
        salt VARCHAR(50)
    );
'''

CREATE_MOVIES = '''
    CREATE TABLE IF NOT EXISTS movies(
        id INTEGER PRIMARY KEY,
        name VARCHAR(50),
        rating REAL CHECK(rating > 0 AND rating <= 10)
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
        row INTEGER CHECK (row > 0 AND row <= 100),
        col INTEGER CHEcK (col > 0 AND col <= 100),
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(projection_id) REFERENCES projection(id)
    );
'''
