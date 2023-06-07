-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 07 Jun 2023 pada 11.05
-- Versi server: 10.3.16-MariaDB
-- Versi PHP: 7.2.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `scraping`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `websc`
--

CREATE TABLE `websc` (
  `id` int(4) NOT NULL,
  `waktu` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `kata` varchar(25) NOT NULL,
  `frekuensi` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data untuk tabel `websc`
--

INSERT INTO `websc` (`id`, `waktu`, `kata`, `frekuensi`) VALUES
(26, '2023-06-07 09:03:08', 'ai', 115),
(27, '2023-06-07 09:03:08', 'teknologi', 105),
(28, '2023-06-07 09:03:08', 'kecerdasan', 103),
(29, '2023-06-07 09:03:08', 'buatan', 76),
(30, '2023-06-07 09:03:08', 'teknik', 63),
(31, '2023-06-07 09:03:08', 'artificial', 51),
(32, '2023-06-07 09:03:08', 'intelligence', 40),
(33, '2023-06-07 09:03:08', 'sistem', 39),
(34, '2023-06-07 09:03:08', '2023,', 34),
(35, '2023-06-07 09:03:08', 'wib', 34),
(36, '2023-06-07 09:03:08', 'belajar', 31),
(37, '2023-06-07 09:03:08', 'juni', 30),
(38, '2023-06-07 09:03:08', 'manusia', 29),
(39, '2023-06-07 09:03:08', 'pembelajaran', 28),
(40, '2023-06-07 09:03:08', 'virtual', 27),
(41, '2023-06-07 09:03:08', 'salah', 25),
(42, '2023-06-07 09:03:08', 'asisten', 24),
(43, '2023-06-07 09:03:08', 'pendidikan', 22),
(44, '2023-06-07 09:03:08', 'bidang', 20),
(45, '2023-06-07 09:03:08', 'komputer', 20),
(46, '2023-06-07 09:03:08', 'memiliki', 20),
(47, '2023-06-07 09:03:08', 'bahasa', 20),
(48, '2023-06-07 09:03:08', 'data', 19),
(49, '2023-06-07 09:03:08', 'contoh', 19),
(50, '2023-06-07 09:03:08', '&', 18);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `websc`
--
ALTER TABLE `websc`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `websc`
--
ALTER TABLE `websc`
  MODIFY `id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=51;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
