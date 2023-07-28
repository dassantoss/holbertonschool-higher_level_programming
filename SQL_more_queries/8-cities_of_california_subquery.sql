-- Script to list all the cities of California.
-- Query to find the state_id for California

SELECT id, name 
FROM cities 
WHERE state_id = (
	SELECT id 
	FROM states 
	WHERE name = 'California')
ORDER BY ID;
