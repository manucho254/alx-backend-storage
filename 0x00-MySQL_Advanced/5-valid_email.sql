-- SQL script that creates a trigger that resets the
-- attribute valid_email only when the email has been changed

DELIMITER $$
CREATE TRIGGER before_update_user
BEFORE UPDATE ON users FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
	IF NEW.email REGEXP '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,4}$' THEN
             SET NEW.valid_email = !NEW.valid_email;
        END IF;
    END IF;
END$$

DELIMITER ;
