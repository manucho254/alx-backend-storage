-- SQL script that creates a trigger that resets the
-- attribute valid_email only when the email has been changed

DELIMITER $$
CREATE TRIGGER before_update_user
BEFORE UPDATE ON users FOR EACH ROW
BEGIN
    SET NEW.valid_email = OLD.valid_email;
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = !OLD.valid_email;
    END IF;
END$$

DELIMITER ;
