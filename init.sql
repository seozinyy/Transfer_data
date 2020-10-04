SET NAMES utf8 ;

DROP TABLE IF EXISTS `test`;
SET character_set_client = utf8mb4 ;

CREATE TABLE `test` (
  `name` varchar(30),
  `age` int
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
