-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 30, 2024 at 07:41 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `simplecoin`
--

-- --------------------------------------------------------

--
-- Table structure for table `account`
--

CREATE TABLE `account` (
  `ID` int(11) NOT NULL,
  `wallet_number` varchar(255) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `balance` float NOT NULL DEFAULT 0,
  `fiat_balance` float NOT NULL,
  `nonce` int(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`ID`, `wallet_number`, `username`, `password`, `balance`, `fiat_balance`, `nonce`) VALUES
(1, '0xmcZgtzzxPc3BmZot7q4xm872Qtr', 'Pahri', 'd527fb06e51963a7742f72707928677d', 100.99, 0, 0),
(2, '0x2PAi7byy8LfmHBLLUtoAF2QB4842', 'putracina', '6aa4db0e2577b4d8acda3c0702e31a8c', 100, 200, 0),
(3, '0xmbU9R2VXTbqASaVREkUujUp77nu', 'alfaridzi', '445efbe30cab3686cb5ca68c60a93d4f', 232, 70, 0),
(4, '0x2Q7nNpnJsRXNguUSo1AbDmJgjdLz', 'smileypuq', 'd2cc7012f3abe763e8e9a68f4b39724f', 11, 0, 0),
(5, '0x2PyB5RvP1xbSCreZuXNAiNmPpHrL', 'faqihjagohyper', 'e807f1fcf82d132f9bb018ca6738a19f', 1.0001, 0, 0),
(6, '0xnZfn2LseArFTErhL1gwPCPtMCJ4', 'admin', '0192023a7bbd73250516f069df18b500', 0.09, 0, 0),
(7, '0x2MYcSGu7g5ntyXoZjARuHCQjNppV', 'halo', 'f98aa3ec36a5b5086c1a93f689259060', 5, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `public_records`
--

CREATE TABLE `public_records` (
  `ID` int(11) NOT NULL,
  `transaction_id` varchar(255) NOT NULL,
  `method` varchar(255) DEFAULT NULL,
  `from_wallet` varchar(255) NOT NULL,
  `to_wallet` varchar(255) NOT NULL,
  `note` varchar(300) NOT NULL,
  `amount` float NOT NULL,
  `fee` float NOT NULL,
  `date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `public_records`
--

INSERT INTO `public_records` (`ID`, `transaction_id`, `method`, `from_wallet`, `to_wallet`, `note`, `amount`, `fee`, `date`) VALUES
(3, '48a0cb465623551118da6ea7c70e98e77f7261c382ef874b29cb8724322e45bc', NULL, '0xmbU9R2VXTbqASaVREkUujUp77nu', '0x2PAi7byy8LfmHBLLUtoAF2QB4842', 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.', 99.99, 0.01, '2024-04-26 08:49:24'),
(4, '6989e5d7561741af24154288aa74f1824266bdf527c12c61f1fa304ee19dcb46', NULL, '0xmbU9R2VXTbqASaVREkUujUp77nu', '0x2PAi7byy8LfmHBLLUtoAF2QB4842', 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.', 9.991, 0.01, '2024-04-26 09:07:43'),
(5, 'd0fcd37bca6e8f7a302826730b1e3bdfd3d0602c172353c8a64e3443d000690a', NULL, '0xmbU9R2VXTbqASaVREkUujUp77nu', '0x2PAi7byy8LfmHBLLUtoAF2QB4842', 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.', 100, 0.01, '2024-04-26 09:09:25'),
(6, '38b6535e027b1c977b66e203fedf033615983ad153b09971a34a85be71f137e4', NULL, '0xmbU9R2VXTbqASaVREkUujUp77nu', '0x2Q7nNpnJsRXNguUSo1AbDmJgjdLz', 'test test', 10, 0.01, '2024-04-26 11:05:27'),
(7, 'b30e00ca580ef233d7731fb14282be31a61c981b38a2fb2bc9520c92c94cbb08', NULL, '0xmbU9R2VXTbqASaVREkUujUp77nu', '0x2Q7nNpnJsRXNguUSo1AbDmJgjdLz', 'asdasdsa', 1, 0.01, '2024-04-26 11:06:45'),
(8, '560dec848e9104f6faecfa9fee1a7da80f4f66c59b3126dbb9403849000c90cb', NULL, '0xmbU9R2VXTbqASaVREkUujUp77nu', '0x2MYcSGu7g5ntyXoZjARuHCQjNppV', 'test test', 5, 0.01, '2024-04-26 11:07:45'),
(9, '73e1e41011a12599529a6cdac654c89c383a406655c1d3cbcaf1cc65c8398f35', NULL, '0xmbU9R2VXTbqASaVREkUujUp77nu', '0xmcZgtzzxPc3BmZot7q4xm872Qtr', 'fdsfsdf', 1, 0.01, '2024-04-26 11:17:23'),
(10, 'aca45c5baba4d730d849cb4672f7037c17fd38e5de3294381d79161231912f53', 'buy', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 20, 0, '2024-04-29 11:40:06'),
(11, '72a0516dc79fbb3d958c3ee17d114e846457555071da69764753e1acc5b4f488', 'SELL', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 20, 0, '2024-04-29 12:41:57'),
(12, 'ae9a3e090c6d501a2a37d8b7783f936dd1a35f466eba062181f1cbbab1e7658a', 'SELL', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 20, 0, '2024-04-29 12:42:15'),
(13, 'b5503aa87b465e73e492d245b1469243e50640e1f819378d9ea24b28603f2f04', 'transfer', '0xmbU9R2VXTbqASaVREkUujUp77nu', '0x2PyB5RvP1xbSCreZuXNAiNmPpHrL', 'minimal kalah jan log out dek', 1, 0.01, '2024-04-29 13:38:26'),
(14, '2f203753cd6da38a03c743c43a656edba8bc6f41c1e050be9f452f1375e96fad', 'BUY', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 100, 0, '2024-04-29 13:57:22'),
(15, '6259b7285449aeed306208bcf906ebe847a35fcf3f8d3dcc1ebd288d2a48ae12', 'BUY', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 10, 0, '2024-04-29 13:57:36'),
(16, '22c38a1d26d375f9c567ef8acf6d5b30994925d9b0dbe77c6c2686b86c622157', 'BUY', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 1, 0, '2024-04-29 14:05:42'),
(17, '416ae0f6a0515f4d8d0b5dc8c04258401b576994a25d4e19908081537843f30f', 'BUY', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 20, 0, '2024-04-30 08:56:16'),
(18, '1975f95d7765132ebf311e89c3ee2e367463f9da769253cb399d41fcf8370403', 'SELL', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 1, 0, '2024-04-30 08:58:01'),
(19, '474e86ba0ef7af9fb223f2b41453ff12c4cc64a61ec1f8612caaafa51fbf951d', 'SELL', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 20, 0, '2024-04-30 08:58:18');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `public_records`
--
ALTER TABLE `public_records`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `public_records`
--
ALTER TABLE `public_records`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
