SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

CREATE TABLE `stock` (
  `id` SERIAL,
  `name` varchar(255) NOT NULL,
  `product_id` varchar(20) NOT NULL,
  `quantity` int NOT NULL,
  `price` int NOT NULL,
  `img` varchar(500) NOT NULL,
  `version` int DEFAULT 0,
  `create_at` DATETIME DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB CHARSET=utf8 COLLATE utf8_general_ci;

ALTER TABLE `stock`
  ADD PRIMARY KEY (`id`);

INSERT INTO `stock` (`name`,`product_id`,`quantity`,`price`,`img`)
VALUES
  ('Nom yen','87N-MsokbrSRCfGlo47t',5,20,'https://i.pinimg.com/564x/95/f1/33/95f13351c09ce433ce4e4666d4ece96c.jpg'),
  ('Pine colada','vXQO_CrfSNy2NSunh_uw',7,33,'https://www.acouplecooks.com/wp-content/uploads/2021/02/Painkiller-Cocktail-008.jpg'),
  ('Blue hawaii','kEvvqXPSuV_ibALTG-lH',2,27,'https://i.pinimg.com/564x/84/87/8d/84878da36d27e4c0603ecd48bee6c548.jpg'),
  ('Blackberry bramble','bZJwf2CL3ezhDwX9pc1J',1,50,'https://i.pinimg.com/564x/72/c2/1d/72c21d9bedadc9a9f6c70847ab5a1b75.jpg'),
  ('Spiced honey','tNOk9lbD9uNh48JleRRm',6,47,'https://i.pinimg.com/564x/a3/4a/c3/a34ac34316afe22ade68c6b2f71ac61e.jpg'),
  ('Frozen cherry','WweBhdrOu3CsEzddF62k',12,35,'https://i.pinimg.com/564x/b4/73/07/b473074a7152a34a722d7bcd7569d69c.jpg'),
  ('Boozy whipped coffee','diFhajwD1cAzm6b_CZ6Z',5,34,'https://i.pinimg.com/564x/3f/d4/e9/3fd4e966debbe4810a4012546a084da2.jpg'),
  ('Dragon drink','tSbkOhOIZTujC9z6C0Mn',9,59,'https://i.pinimg.com/564x/6b/d9/14/6bd914ab6f2d87ad91f7caf41ac4a485.jpg'),
  ('Strawberry refresh','8W4r8cZv-S_lQkPMhUZR',3,41,'https://i.pinimg.com/564x/7a/2f/5e/7a2f5eb2756be7ebfed60e2c70d84a21.jpg'),
  ('Bluepi drink','i_K45QJ7SBYX4ErZHxnc',2,60,'https://i.pinimg.com/564x/84/a8/a2/84a8a27257396713b6cf24713ecc095b.jpg');

COMMIT;
