SQLInjection:
	SELECT * FROM users
		WHERE (username='Ashsih')
		AND (password = '1' OR '1' = '1')
Race Condition:
	