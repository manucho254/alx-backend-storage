-- SQL script that creates an index idx_name_first_score
-- on the table names and the first letter of name and the score.

-- Create an index on the new column
CREATE INDEX idx_name_first_score ON names (name(1), LEFT(CAST(score AS CHAR), 1));
