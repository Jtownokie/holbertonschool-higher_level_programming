-- Selects all rows where name is not null and orders by score DESC
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
