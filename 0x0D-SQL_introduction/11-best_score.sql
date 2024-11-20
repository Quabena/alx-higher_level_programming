-- A script that lists records with score >= 10 from second_table
-- Syntax: SELECT fields FROM table_name WHERE condition ORDER BY column_name DESC

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
