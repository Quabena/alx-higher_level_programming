-- A script that counts records with the same score in second_table
-- Syntax: SELECT column_name, COUNT(*) AS alias_name FROM table_name GROUP BY column_name ORDER BY alias_name DESC

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
