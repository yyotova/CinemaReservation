SELECT_USER = f'''
SELECT email
FROM users
WHERE email = ? AND password = ?;
'''
