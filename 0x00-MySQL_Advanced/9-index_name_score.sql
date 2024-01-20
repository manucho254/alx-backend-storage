-- SQL script that creates an index idx_name_first_score
-- on the table names and the first letter of name and the score.

-- Add a new column to store the first value
ALTER TABLE names
ADD COLUMN first_val INT;

-- Update the new column with the first value of your_column
UPDATE names
SET first_val = CAST(SUBSTRING(CAST(score AS CHAR), 1, 1) AS UNSIGNED);

-- Create an index on the new column
CREATE INDEX idx_name_first_score ON names (name(1), first_val);
