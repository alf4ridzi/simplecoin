-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 29, 2024 at 03:37 AM
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
  `nonce` varchar(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `account`
--

INSERT INTO `account` (`ID`, `wallet_number`, `username`, `password`, `balance`, `fiat_balance`, `nonce`) VALUES
(1, '0xmcZgtzzxPc3BmZot7q4xm872Qtr', 'Pahri', 'd527fb06e51963a7742f72707928677d', 100.99, 0, '0'),
(2, '0x2PAi7byy8LfmHBLLUtoAF2QB4842', 'putracina', '6aa4db0e2577b4d8acda3c0702e31a8c', 100, 200, '0'),
(3, '0xmbU9R2VXTbqASaVREkUujUp77nu', 'alfaridzi', '445efbe30cab3686cb5ca68c60a93d4f', 122, 90, '0'),
(4, '0x2Q7nNpnJsRXNguUSo1AbDmJgjdLz', 'smileypuq', 'd2cc7012f3abe763e8e9a68f4b39724f', 11, 0, '0'),
(5, '0x2PyB5RvP1xbSCreZuXNAiNmPpHrL', 'faqihjagohyper', 'e807f1fcf82d132f9bb018ca6738a19f', 1.0001, 0, '0'),
(6, '0xnZfn2LseArFTErhL1gwPCPtMCJ4', 'admin', '0192023a7bbd73250516f069df18b500', 0.201, 0, '0'),
(7, '0x2MYcSGu7g5ntyXoZjARuHCQjNppV', 'halo', 'f98aa3ec36a5b5086c1a93f689259060', 5, 0, '0'),
(8, '0xgupdnRvvjSiRuQCVbeTi94k4dMK', 'paripari123', '688e4b06ddfe05ada7700e33e7c3a02c', 21, 0, '0'),
(9, '0xjzU8o9vhBv5TksyXuqqd38qpBME', 'damarpoke77', '34230f8fa06727cc0b0a786c325cdd41', 130, 100, '0'),
(10, '0x2QnFvYX1ahTABzasyeynqNRbbsjh', 'kelinghitam', '1749f2802381694c23375c61e2bcb7d7', 100, 0, '0'),
(11, '0xiXtMfkmTtMCpJPv9xkmLXZ5qSNj', 'alfaridzi2', '445efbe30cab3686cb5ca68c60a93d4f', 270, 100, '0');

-- --------------------------------------------------------

--
-- Table structure for table `nonce`
--

CREATE TABLE `nonce` (
  `ID` int(11) NOT NULL,
  `transaction_id` varchar(255) NOT NULL DEFAULT '0',
  `nonce` varchar(6) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `nonce`
--

INSERT INTO `nonce` (`ID`, `transaction_id`, `nonce`) VALUES
(1, '3e3337b17a890037a194e8fa3ef11b56f357f0565723080907632b01dc8da020', '0'),
(2, '3dd8e4be3a2b6225aa711499967580f919a13fcebb76f34db3f25aa50839fe6f', '5'),
(3, '9b737b52f6e56f75bcbd7e2f99b7eb8e10ec782753afa3b833e2d0f52783cf19', 'i4i67d');

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
  `date` datetime NOT NULL DEFAULT current_timestamp(),
  `status` varchar(255) NOT NULL DEFAULT 'PENDING'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `public_records`
--

INSERT INTO `public_records` (`ID`, `transaction_id`, `method`, `from_wallet`, `to_wallet`, `note`, `amount`, `fee`, `date`, `status`) VALUES
(3, '48a0cb465623551118da6ea7c70e98e77f7261c382ef874b29cb8724322e45bc', NULL, '0xmbU9R2VXTbqASaVREkUujUp77nu', '0x2PAi7byy8LfmHBLLUtoAF2QB4842', 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.', 99.99, 0.01, '2024-04-26 08:49:24', 'PENDING'),
(4, '6989e5d7561741af24154288aa74f1824266bdf527c12c61f1fa304ee19dcb46', NULL, '0xmbU9R2VXTbqASaVREkUujUp77nu', '0x2PAi7byy8LfmHBLLUtoAF2QB4842', 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.', 9.991, 0.01, '2024-04-26 09:07:43', 'PENDING'),
(5, 'd0fcd37bca6e8f7a302826730b1e3bdfd3d0602c172353c8a64e3443d000690a', NULL, '0xmbU9R2VXTbqASaVREkUujUp77nu', '0x2PAi7byy8LfmHBLLUtoAF2QB4842', 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks.', 100, 0.01, '2024-04-26 09:09:25', 'PENDING'),
(6, '38b6535e027b1c977b66e203fedf033615983ad153b09971a34a85be71f137e4', NULL, '0xmbU9R2VXTbqASaVREkUujUp77nu', '0x2Q7nNpnJsRXNguUSo1AbDmJgjdLz', 'test test', 10, 0.01, '2024-04-26 11:05:27', 'PENDING'),
(7, 'b30e00ca580ef233d7731fb14282be31a61c981b38a2fb2bc9520c92c94cbb08', NULL, '0xmbU9R2VXTbqASaVREkUujUp77nu', '0x2Q7nNpnJsRXNguUSo1AbDmJgjdLz', 'asdasdsa', 1, 0.01, '2024-04-26 11:06:45', 'PENDING'),
(8, '560dec848e9104f6faecfa9fee1a7da80f4f66c59b3126dbb9403849000c90cb', NULL, '0xmbU9R2VXTbqASaVREkUujUp77nu', '0x2MYcSGu7g5ntyXoZjARuHCQjNppV', 'test test', 5, 0.01, '2024-04-26 11:07:45', 'PENDING'),
(9, '73e1e41011a12599529a6cdac654c89c383a406655c1d3cbcaf1cc65c8398f35', NULL, '0xmbU9R2VXTbqASaVREkUujUp77nu', '0xmcZgtzzxPc3BmZot7q4xm872Qtr', 'fdsfsdf', 1, 0.01, '2024-04-26 11:17:23', 'PENDING'),
(10, 'aca45c5baba4d730d849cb4672f7037c17fd38e5de3294381d79161231912f53', 'buy', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 20, 0, '2024-04-29 11:40:06', 'PENDING'),
(11, '72a0516dc79fbb3d958c3ee17d114e846457555071da69764753e1acc5b4f488', 'SELL', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 20, 0, '2024-04-29 12:41:57', 'PENDING'),
(12, 'ae9a3e090c6d501a2a37d8b7783f936dd1a35f466eba062181f1cbbab1e7658a', 'SELL', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 20, 0, '2024-04-29 12:42:15', 'PENDING'),
(13, 'b5503aa87b465e73e492d245b1469243e50640e1f819378d9ea24b28603f2f04', 'transfer', '0xmbU9R2VXTbqASaVREkUujUp77nu', '0x2PyB5RvP1xbSCreZuXNAiNmPpHrL', 'minimal kalah jan log out dek', 1, 0.01, '2024-04-29 13:38:26', 'PENDING'),
(14, '2f203753cd6da38a03c743c43a656edba8bc6f41c1e050be9f452f1375e96fad', 'BUY', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 100, 0, '2024-04-29 13:57:22', 'PENDING'),
(15, '6259b7285449aeed306208bcf906ebe847a35fcf3f8d3dcc1ebd288d2a48ae12', 'BUY', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 10, 0, '2024-04-29 13:57:36', 'PENDING'),
(16, '22c38a1d26d375f9c567ef8acf6d5b30994925d9b0dbe77c6c2686b86c622157', 'BUY', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 1, 0, '2024-04-29 14:05:42', 'PENDING'),
(17, '416ae0f6a0515f4d8d0b5dc8c04258401b576994a25d4e19908081537843f30f', 'BUY', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 20, 0, '2024-04-30 08:56:16', 'PENDING'),
(18, '1975f95d7765132ebf311e89c3ee2e367463f9da769253cb399d41fcf8370403', 'SELL', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 1, 0, '2024-04-30 08:58:01', 'PENDING'),
(19, '474e86ba0ef7af9fb223f2b41453ff12c4cc64a61ec1f8612caaafa51fbf951d', 'SELL', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 20, 0, '2024-04-30 08:58:18', 'PENDING'),
(20, '3a481203bb0b25bcd1ff6d80faa5d6c18984ab61d5d828d0f74a447465cbab54', 'SELL', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 21, 0, '2024-04-30 12:42:03', 'PENDING'),
(21, '26be2ba72444655ed784d9c63f8a20f1e98cbb65f3cab3a8b4fbf8b71e09d952', 'SELL', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 9, 0, '2024-04-30 12:42:20', 'PENDING'),
(22, '8a53786a996fbb71265cfefd258633354fc982655af764ba2869efa104260eb9', 'SELL', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 20, 0, '2024-04-30 12:45:17', 'PENDING'),
(23, 'b0df5e17327586cc865460e789e91f5856d3699fcd3791ad4a6547ba4c8789ce', 'BUY', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 120, 0, '2024-04-30 12:45:32', 'PENDING'),
(24, '0243a1aa521d988feb9b52ac295eb7af42f04ca2d60328b9c853de6fbb698dcc', 'SELL', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 1, 0, '2024-04-30 12:59:55', 'PENDING'),
(25, 'f64193a48abc9377feba31b15e1b2eb30570409fae4ac3ce881c1227f5d0709f', 'Deposit Dana', '', '0xgupdnRvvjSiRuQCVbeTi94k4dMK', '', 100, 0, '2024-05-03 07:22:19', 'PENDING'),
(26, 'c339d606d72d1a2e3b891feca2c9c9ea184ce343ffc89707f046c57d0c834e81', 'BUY', '', '0xgupdnRvvjSiRuQCVbeTi94k4dMK', '', 100, 0, '2024-05-03 07:22:59', 'PENDING'),
(27, '785af84aa6555bc52d5c231aec59b98ea9589ab2f9078b1b4e025826fb85c344', 'SELL', '', '0xgupdnRvvjSiRuQCVbeTi94k4dMK', '', 100, 0, '2024-05-03 07:23:10', 'PENDING'),
(28, '7d0c2268fb983b5e8f6ae24d6d2b9e8eb3317d4cc4a85befed4da5095df77152', 'BUY', '', '0xgupdnRvvjSiRuQCVbeTi94k4dMK', '', 100, 0, '2024-05-03 07:25:03', 'PENDING'),
(29, '1f431ef5a9996207879bda76ebd9fa3156b07ea51e6508f3fc0b24a0aff3dcec', 'TRANSFER', '0xgupdnRvvjSiRuQCVbeTi94k4dMK', '0xmbU9R2VXTbqASaVREkUujUp77nu', 'alamak', 99, 0.01, '2024-05-03 07:25:19', 'PENDING'),
(30, 'f20f7f61e4f47f46f815a713989b2fc281845261f29947d6dcf8401c68be5cc6', 'TRANSFER', '0xmbU9R2VXTbqASaVREkUujUp77nu', '0xgupdnRvvjSiRuQCVbeTi94k4dMK', 'makasih', 100, 0.01, '2024-05-03 07:26:59', 'PENDING'),
(31, 'b7a24fd049105557931f5a6237cc24f8e8ffdb71864252edda2f1ec37247a243', 'TRANSFER', '0xgupdnRvvjSiRuQCVbeTi94k4dMK', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 50, 0.01, '2024-05-03 07:28:37', 'PENDING'),
(32, '3d74ea53a8306efb3b1f8953c532a0d83e05e8e585a611dc8e191a9f0b7f0962', 'TRANSFER', '0xgupdnRvvjSiRuQCVbeTi94k4dMK', '0xjzU8o9vhBv5TksyXuqqd38qpBME', 'Depo depo menyala', 30, 0.01, '2024-05-03 07:34:50', 'PENDING'),
(33, 'bc0d3a169dfcbaf93e1efd54f0f72c5acab5e475e90afbe52734acda606fd2e7', 'TRANSFER', '0xmbU9R2VXTbqASaVREkUujUp77nu', '0xjzU8o9vhBv5TksyXuqqd38qpBME', 'jangan depo mlu mar', 100, 0.01, '2024-05-03 07:35:21', 'PENDING'),
(34, '2ae2ef361e1547735599adc88be509987b7d2f4da1aa46ab3ac1c17a0bb451d2', 'Deposit Dana', '', '0xjzU8o9vhBv5TksyXuqqd38qpBME', '', 100, 0, '2024-05-03 07:36:01', 'PENDING'),
(35, 'ec522d55add4de8def281085fb2489421914a7f58fc9c8e86f7c683e49ac3822', 'TRANSFER', '0xmbU9R2VXTbqASaVREkUujUp77nu', '0x2QnFvYX1ahTABzasyeynqNRbbsjh', 'cina', 100, 0.01, '2024-05-03 08:01:29', 'PENDING'),
(36, '6caed604c4267703e853c9680d273b64781cf8b1c623e5288df71b8da6e314d0', 'TRANSFER', '0xmbU9R2VXTbqASaVREkUujUp77nu', '0xiXtMfkmTtMCpJPv9xkmLXZ5qSNj', 'test', 19, 0.01, '2024-05-06 11:05:44', 'PENDING'),
(37, '989c4448172652381fb2cc8d585e08e2d1408086b9cd4ef08ce2d7ca1eab13e4', 'Deposit Dana', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 10, 0, '2024-05-06 11:06:57', 'PENDING'),
(38, '7d4b32099e4a89b865dd76f6ad2c22d37750075e857d4707fd4766c64be204e3', 'Deposit Dana', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 20, 0, '2024-05-06 11:07:06', 'PENDING'),
(39, 'd2159663f1b85eb103dfae167433f3bc767b08b5e0f347b1eedf753b3220186d', 'BUY', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 31, 0, '2024-05-06 11:07:30', 'PENDING'),
(40, '2266fb34f0450366d94ff3fbfcaee793a1d0352de5a1fc3da06bd5cd96cea794', 'SELL', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 162, 0, '2024-05-06 11:07:51', 'PENDING'),
(41, '62b25b04dbf19ee01f7cd7f81b10e67cdf45f11e0cdc30fbdd4c2bae4a89bce4', 'BUY', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 162, 0, '2024-05-13 11:16:36', 'PENDING'),
(42, 'e83113dda50b71c8315d4942c9d4f7a1ef15ebe9a5b62d72d8faec3d6edf2172', 'SELL', '', '0xiXtMfkmTtMCpJPv9xkmLXZ5qSNj', '', 19, 0, '2024-05-13 11:16:50', 'PENDING'),
(43, 'd6644e206756689604cb06d16b78803a741e2e4cf70f03d7dbe81227239aad17', 'TRANSFER', '0xmbU9R2VXTbqASaVREkUujUp77nu', '0xiXtMfkmTtMCpJPv9xkmLXZ5qSNj', 'test', 111, 0.01, '2024-05-13 11:17:08', 'PENDING'),
(44, '4a06f2175e4a47bb14b722ced069e5da52da417519803bc308f55b20ffdbfe68', 'Deposit OVO', '', '0xiXtMfkmTtMCpJPv9xkmLXZ5qSNj', '', 100, 0, '2024-05-13 11:17:48', 'PENDING'),
(45, '35c5d6773506cb6d4fc936f9fdd8568275757fbb2a43a9e6e003c93e984f9a4e', 'BUY', '', '0xiXtMfkmTtMCpJPv9xkmLXZ5qSNj', '', 119, 0, '2024-05-13 11:18:05', 'PENDING'),
(46, '1d27ffd756787a56319ede096c362e8a9c50e71320ff1bef8062702c7456b800', 'TRANSFER', '0xiXtMfkmTtMCpJPv9xkmLXZ5qSNj', '0xmbU9R2VXTbqASaVREkUujUp77nu', 'test test', 100, 0.01, '2024-05-13 11:18:31', 'PENDING'),
(47, '9cf317f290fdf324aec2f10050e23e8063ca2464de6aa194f4cbcf744bccb2cc', 'TRANSFER', '0xmbU9R2VXTbqASaVREkUujUp77nu', '0xiXtMfkmTtMCpJPv9xkmLXZ5qSNj', 'kirim', 150, 0.01, '2024-05-13 11:19:51', 'PENDING'),
(48, '980fc541e08a799a77ab0e14462b5f4f5d9542ab689d459769bd1efc08cc17e0', 'Deposit Dana', '', '0xiXtMfkmTtMCpJPv9xkmLXZ5qSNj', '', 100, 0, '2024-05-13 11:20:37', 'PENDING'),
(49, '9691907b3716921492ac72c8ecf13d9654710a2344e767bc7221de50af8d28f9', 'TRANSFER', '0xiXtMfkmTtMCpJPv9xkmLXZ5qSNj', '0xmbU9R2VXTbqASaVREkUujUp77nu', 'test', 20, 0.01, '2024-05-13 11:22:08', 'PENDING'),
(50, 'f9f9a05c2b9bc6fde77896d6d44176865c8aee1a3b5eee10e175e2488a1a4326', 'Deposit Jenius', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 200, 0, '2024-05-15 11:29:52', 'PENDING'),
(51, '6693a6dd926bd53b45a4aba117f5a650c01c25e2f71f46d35b7ba98d16cd2100', 'TRANSFER', '0xmbU9R2VXTbqASaVREkUujUp77nu', '0xiXtMfkmTtMCpJPv9xkmLXZ5qSNj', 'sdfsdf', 10, 0.001, '2024-05-29 08:19:18', 'PENDING'),
(52, '10776e54cb122bcb9f9e6d86ed1de90319d94b498aa5b2c563e3217934a59f20', 'BUY', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 100, 0, '2024-05-29 08:19:31', 'PENDING'),
(53, '1af10f063f872138670bb5672c33d81cd0d7cc5240e630d24ebb14b411f2d734', 'Deposit Dana', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 1, 0, '2024-05-29 08:19:43', 'PENDING'),
(54, '0211764489285c38c31d14cccdde620740ca198f3ea4d6d9987e760bfa031efb', 'SELL', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 100, 0, '2024-05-29 08:19:52', 'PENDING'),
(55, '3e3337b17a890037a194e8fa3ef11b56f357f0565723080907632b01dc8da020', 'BUY', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 100, 0, '2024-05-29 08:33:53', 'PENDING'),
(56, '3dd8e4be3a2b6225aa711499967580f919a13fcebb76f34db3f25aa50839fe6f', 'BUY', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 10, 0, '2024-05-29 08:35:05', 'PENDING'),
(57, '9b737b52f6e56f75bcbd7e2f99b7eb8e10ec782753afa3b833e2d0f52783cf19', 'BUY', '', '0xmbU9R2VXTbqASaVREkUujUp77nu', '', 1, 0, '2024-05-29 08:35:26', 'PENDING');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `account`
--
ALTER TABLE `account`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `nonce`
--
ALTER TABLE `nonce`
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
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `nonce`
--
ALTER TABLE `nonce`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `public_records`
--
ALTER TABLE `public_records`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=58;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
