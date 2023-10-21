-- Computes average of all records
ALTER TABLE second_table ADD average INT;
UPDATE second_table SET average = (SELECT AVG(score) FROM second_table);
