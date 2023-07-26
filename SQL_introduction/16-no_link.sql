-- Task 16
-- List all records excluding rows without a name value.

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
