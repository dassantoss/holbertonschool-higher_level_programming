-- Script to create the database hbtn_0d_usa and the table states.
-- Query to create the database hbtn_0d_usa if not exists.

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
		id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
		name VARCHAR(256) NOT NULL
);
