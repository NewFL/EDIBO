USE db24;
CREATE TABLE `MyTBL_3b` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Title` varchar(20) NOT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


/* DELIMITER $$
CREATE TRGIGGER MyTBL_3a_guard1 BEFORE INSERT ON MyTBL_3a
FOR EACH TOW
BEGIN
declare a varchar(100);
SIGNAL CURRENT_USER() INTO @a;
SIGNAL SQLSTATE '50000' SET message_text=@a;
END; $$
DELIMITER ;


INSERT INTO MyTBL_3a (Title) Value ('AAA');
*/