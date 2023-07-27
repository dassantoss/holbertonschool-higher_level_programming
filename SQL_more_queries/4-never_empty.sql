-- Script that creates the table id_not_null on your MySQL server.
-- Query to create the table id_not_null.

CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1,
	name VARCHAR(256)
);
