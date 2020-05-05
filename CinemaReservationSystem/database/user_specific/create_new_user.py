INSERT_USER = f'''
INSERT INTO users (email, password, salt)
VALUES (?, ?, ?);
'''
