-- SQL script that creates a stored procedure
-- ComputeAverageScoreForUser that computes
-- and store the average score for a student

DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
   SELECT AVG(corrections.score) INTO @user_average
   FROM corrections WHERE user_id = user_id;

   UPDATE users SET average_score = @user_average WHERE id = user_id;
END//
DELIMITER ;
