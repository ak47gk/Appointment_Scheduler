-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 11, 2021 at 01:35 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `scheduler`
--

-- --------------------------------------------------------

--
-- Table structure for table `patient_info`
--

CREATE TABLE `patient_info` (
  `id` int(11) NOT NULL,
  `serial` text NOT NULL,
  `first_name` text NOT NULL,
  `last_name` text NOT NULL,
  `age` text NOT NULL,
  `gender` text NOT NULL,
  `city` text NOT NULL,
  `mail` text NOT NULL,
  `address` text NOT NULL,
  `phone` text NOT NULL,
  `reason` text NOT NULL,
  `start_time` text NOT NULL,
  `end_time` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patient_info`
--

INSERT INTO `patient_info` (`id`, `serial`, `first_name`, `last_name`, `age`, `gender`, `city`, `mail`, `address`, `phone`, `reason`, `start_time`, `end_time`) VALUES
(8, '1', 'Rafiul', 'Islam', '20', 'male', 'Dhaka', 'rafiul@gmail.com', '01111111111', 'Dhaka', 'Fever', '8:00', '8:30');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `patient_info`
--
ALTER TABLE `patient_info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `patient_info`
--
ALTER TABLE `patient_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
