-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 17, 2016 at 04:58 PM
-- Server version: 5.5.53-0ubuntu0.14.04.1
-- PHP Version: 5.5.9-1ubuntu4.20

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `Ocean`
--

-- --------------------------------------------------------

--
-- Table structure for table `Messages`
--

CREATE TABLE IF NOT EXISTS `Messages` (
  `Data` text NOT NULL,
  `Title` varchar(50) NOT NULL,
  `Posttime` varchar(30) NOT NULL,
  `UnameTo` varchar(30) NOT NULL,
  `UnameSent` varchar(30) NOT NULL,
  `mID` int(20) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`mID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=30 ;

--
-- Dumping data for table `Messages`
--

INSERT INTO `Messages` (`Data`, `Title`, `Posttime`, `UnameTo`, `UnameSent`, `mID`) VALUES
('aids', '', '0000-00-00', '', 'test4', 1),
('O Baby I''ll eliminate your 3.5mm headphone jack', '', '0000-00-00', '', 'test4', 3),
('Whats good in the hood?', '', '0000-00-00', '', 'test4', 4),
('ROFLCOPTER', '', '0000-00-00', '', 'test4', 5),
('ME BOOTY', '', '0000-00-00', '', 'test4', 6),
('yaaaaaaaasss kween', '', '69', '', 'test4', 7),
('im so tired', '', '0000-00-00', '', 'test4', 9),
('oh geez', '', '0000-00-00', '', 'test4', 10),
('SMD', '', '0000-00-00', '', 'test4', 11),
('#GoJackets', 'Hello', '0000-00-00', '', 'test4', 12),
('fuq u lol', 'A message to the haters', 'Mon 14 Nov 2016 23:31:55 GMT', '', 'test4', 13),
('CHAYNAHCHAYNAHCHAYNAHMURICACHAYNAHCHAYNAHCHAYNAH', 'China!', '11/14/2016 7:16:19 PM', '', 'test4', 14),
('USAUSAUSUAUSUA', 'AMERICA!', '11/14/2016 7:22:11 PM', '', 'test4', 17),
('Things have to be dolled up nowadays; that''s why they put brass on battleships.', 'Inspirational quote', '11/14/2016  7:23:15 PM', '', 'test4', 18),
('Life imitates art -O.W.', 'Thoughts for food', '11/14/2016  8:13:26 PM', '', '', 19),
('Cheers ye weary powerdermonkeys! The crow''s nest sights land ahead! A round o'' grog for ye all.', 'LAND HOOOO', '11/14/2016  8:56:03 PM', '', '', 20),
('Eyy bb u wan sum fuk?', '', '', '', 'test4', 22);

-- --------------------------------------------------------

--
-- Table structure for table `Users`
--

CREATE TABLE IF NOT EXISTS `Users` (
  `UserName` varchar(30) NOT NULL,
  `Pass` varchar(100) NOT NULL,
  `Salt` varchar(100) NOT NULL,
  `UID` int(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Users`
--

INSERT INTO `Users` (`UserName`, `Pass`, `Salt`, `UID`) VALUES
('baseTest', 'notReal', 'notReal', 0),
('testPassword1!', 'Password1!', '2016-11-01 14:0', 1),
('test1', 'ad152d7dbf8d3d636b5660cc330a52', '2016-11-01 14:1', 1),
('test2', '5bfc8d1a35e0b8f0eaa6bd81734a8b', '2016-11-01 15:2', 1),
('test3', '81cdfb0c595c3dac94cd3e1f7efbbee72a9cd0b394cf2d22fcc7aa85fe72e008', '2016-11-01 15:26:30.988000', 1),
('test4', '68931e2f709393d9e3298a618d22d1c281d26c2c8547e884d69a5c99f0ff2470', '2016-11-01 15:42:20.376000', 1),
('test4', '430b26066fd1fc6f65f1e48c2bf0b4dc1d4624f71506796ff31a6febd22284e1', '2016-11-01 15:43:47.498000', 1),
('tyler', 'c97c3c3b2be039dc073b12569a4e71f5e541305903f65607280a93db28f3bbd4', '2016-11-15 04:28:58.462240', 1),
('knight', 'e0740cdd222861f5b9a795c92ea5df4d21c8ad42ccb05bba331d40f879f87e0b', '2016-11-15 05:05:49.112345', 1);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
