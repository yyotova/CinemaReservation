INSERT_SESSION = f'''
INSERT INTO session (email)
VALUES (?);
'''

SELECT_SESSION = f'''
SELECT email
FROM session;
'''

DELETE_SESSION = f'''
DELETE FROM session;
'''
