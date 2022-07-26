SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `cashbag` (
  `id` SERIAL,
  `value` int NOT NULL,
  `quantity` int NOT NULL,
  `active` int DEFAULT 1,
  `create_at` DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB CHARSET=utf8 COLLATE utf8_general_ci;

ALTER TABLE `cashbag`
  ADD PRIMARY KEY (`id`);

INSERT INTO `cashbag` (`value`, `quantity`)
VALUES 
	(1000, 5),
  (500, 40),
  (100,100),
  (50,200),
  (20,400),
  (10,500),
  (5,500),
  (1,1000);

COMMIT;
