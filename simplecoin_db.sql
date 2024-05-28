-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 19, 2024 at 03:26 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

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
  `password` varchar(255) DEFAULT NULL,
  `balance` float NOT NULL DEFAULT 0,
  `fiat_balance` float NOT NULL DEFAULT 0,
  `nonce` int(6) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`ID`, `wallet_number`, `username`, `password`, `balance`, `fiat_balance`, `nonce`) VALUES
(1, '0xmcZgtzzxPc3BmZot7q4xm872Qtr', 'Pahri', 'd527fb06e51963a7742f72707928677d', 100.99, 0, 0),
(2, '0x2PAi7byy8LfmHBLLUtoAF2QB4842', 'putracina', '6aa4db0e2577b4d8acda3c0702e31a8c', 90, 200, 0),
(3, '0xmbU9R2VXTbqASaVREkUujUp77nu', 'alfaridzi', '445efbe30cab3686cb5ca68c60a93d4f', 122, 890, 0),
(4, '0x2Q7nNpnJsRXNguUSo1AbDmJgjdLz', 'smileypuq', 'd2cc7012f3abe763e8e9a68f4b39724f', 21, 0, 0),
(5, '0x2PyB5RvP1xbSCreZuXNAiNmPpHrL', 'faqihjagohyper', 'e807f1fcf82d132f9bb018ca6738a19f', 1.0001, 0, 0),
(6, '0xnZfn2LseArFTErhL1gwPCPtMCJ4', 'admin', '0192023a7bbd73250516f069df18b500', 0.12, 0, 0),
(7, '0x2MYcSGu7g5ntyXoZjARuHCQjNppV', 'halo', 'f98aa3ec36a5b5086c1a93f689259060', 15, 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `account`
--
ALTER TABLE `account`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
