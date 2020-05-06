SELECT_SALT = f'''
SELECT salt
FROM users
WHERE salt = ?;
'''

SELECT_SALT_USER = f'''
SELECT salt
FROM users
WHERE email = ?;
'''

SELECT_USER = f'''
SELECT email
FROM users
WHERE email = ? AND password = ?;
'''

SELECT_USER_EMAIL = f'''
SELECT email
FROM users
WHERE email = ? ;
'''

INSERT_USER = f'''
INSERT INTO users (email, password, salt)
VALUES (?, ?, ?);
'''
