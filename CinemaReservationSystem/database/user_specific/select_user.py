SELECT_USER = f'''
SELECT username
FROM users
WHERE username = ? AND password = ?;
'''
