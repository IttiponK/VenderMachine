SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `transaction` (
  `id` SERIAL,
  `name` varchar(255) NOT NULL,
  `product_id` varchar(255) NOT NULL,
  `quantity` int NOT NULL,
  `total_amount` int NOT NULL,
  `pay_amount` int NOT NULL,
  `pay_amount_detail` varchar(500) NOT NULL,
  `change` int NOT NULL,
  `change_detail` varchar(255) NOT NULL,
  `create_at` DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB CHARSET=utf8 COLLATE utf8_general_ci;

ALTER TABLE `transaction`
  ADD PRIMARY KEY (`id`);

COMMIT;
