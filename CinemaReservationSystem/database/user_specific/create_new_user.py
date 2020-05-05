INSERT_USER = f'''
INSERT INTO users (username, password, salt)
VALUES (?, ?, ?);
'''
