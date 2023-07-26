-- Task 11
-- List all records with a score >= 10 from the second_table sorted by the score column.

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
