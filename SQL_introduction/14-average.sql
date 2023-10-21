-- Computes average of all records
ALTER TABLE second_table ADD average INT;
INSERT INTO second_table(average) VALUES(SELECT AVG(score) FROM second_table);
