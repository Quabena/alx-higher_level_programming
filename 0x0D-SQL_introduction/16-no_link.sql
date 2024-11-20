-- A script that lists records of second_table with specific conditions
-- Syntax: SELECT column_names FROM table_name WHERE condition ORDER BY column_name DESC

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
