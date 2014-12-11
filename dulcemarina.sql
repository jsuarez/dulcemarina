-- phpMyAdmin SQL Dump
-- version 4.0.6
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Dec 11, 2014 at 09:02 PM
-- Server version: 5.6.20
-- PHP Version: 5.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `dulcemarina`
--

-- --------------------------------------------------------

--
-- Table structure for table `ajustes_sitio`
--

CREATE TABLE IF NOT EXISTS `ajustes_sitio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo_sitio` varchar(65),
  `descripcion_sitio` longtext NOT NULL,
  `mail_sitio` varchar(75) NOT NULL,
  `pub_date` time NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `ajustes_sitio`
--

INSERT INTO `ajustes_sitio` (`id`, `titulo_sitio`, `descripcion_sitio`, `mail_sitio`, `pub_date`) VALUES
(1, 'Dulce Marina » Repostería Argentina - Brasilera en Mendoza', 'descripción del sitio web', 'info@mydesign.com.ar', '19:33:16');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=37 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add producto', 7, 'add_producto'),
(20, 'Can change producto', 7, 'change_producto'),
(21, 'Can delete producto', 7, 'delete_producto'),
(22, 'Can add servicio', 8, 'add_servicio'),
(23, 'Can change servicio', 8, 'change_servicio'),
(24, 'Can delete servicio', 8, 'delete_servicio'),
(25, 'Can add imagen', 9, 'add_imagen'),
(26, 'Can change imagen', 9, 'change_imagen'),
(27, 'Can delete imagen', 9, 'delete_imagen'),
(28, 'Can add foto', 10, 'add_foto'),
(29, 'Can change foto', 10, 'change_foto'),
(30, 'Can delete foto', 10, 'delete_foto'),
(31, 'Can add quienes somos', 11, 'add_quienessomos'),
(32, 'Can change quienes somos', 11, 'change_quienessomos'),
(33, 'Can delete quienes somos', 11, 'delete_quienessomos'),
(34, 'Can add sitio', 12, 'add_sitio'),
(35, 'Can change sitio', 12, 'change_sitio'),
(36, 'Can delete sitio', 12, 'delete_sitio');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$12000$bJYv4qsBbkTH$sdMU4o/OHOOGv+O9jhPhkRZSI8FoRELqq6zQ6/tQhBA=', '2014-12-05 18:48:19', 1, 'mydesign', '', '', 'jsuarez@mydesign.com.ar', 1, 1, '2014-10-29 21:10:56'),
(2, 'pbkdf2_sha256$12000$QLt9RpSf6qPx$S/f9dFNTygJSZYC2H0jIiI0cSBXzIxVx4ZFgBkWdJn4=', '2014-10-29 21:12:14', 0, 'admin', '', '', '', 0, 1, '2014-10-29 21:12:14');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=15 ;

--
-- Dumping data for table `auth_user_user_permissions`
--

INSERT INTO `auth_user_user_permissions` (`id`, `user_id`, `permission_id`) VALUES
(3, 2, 19),
(4, 2, 20),
(5, 2, 21),
(6, 2, 22),
(7, 2, 23),
(8, 2, 24),
(9, 2, 25),
(10, 2, 26),
(11, 2, 27),
(12, 2, 28),
(13, 2, 29),
(14, 2, 30),
(1, 2, 32),
(2, 2, 35);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=41 ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2014-10-29 21:12:14', '2', 'admin', 1, '', 4, 1),
(2, '2014-11-05 21:49:32', '1', 'Servicio object', 1, '', 8, 1),
(3, '2014-11-05 21:49:50', '1', 'Servicio object', 2, 'No ha modificado ningún campo.', 8, 1),
(4, '2014-11-07 21:06:58', '1', 'Servicio object', 3, '', 8, 1),
(5, '2014-11-07 22:16:39', '2', 'Servicio object', 1, '', 8, 1),
(6, '2014-11-19 20:03:13', '1', 'Foto object', 1, '', 10, 1),
(7, '2014-11-19 21:51:43', '1', 'Sitio object', 1, '', 12, 1),
(8, '2014-11-19 21:54:25', '1', 'QuienesSomos object', 1, '', 11, 1),
(9, '2014-12-01 19:33:16', '1', 'Sitio object', 2, 'No ha modificado ningún campo.', 12, 1),
(10, '2014-12-01 19:49:27', '1', 'QuienesSomos object', 2, 'No ha modificado ningún campo.', 11, 1),
(11, '2014-12-03 22:05:17', '1', 'Producto object', 1, '', 7, 1),
(12, '2014-12-03 22:18:43', '1', 'QuienesSomos object', 2, 'Modifica descripcion_nosotros.', 11, 1),
(13, '2014-12-03 22:23:38', '2', 'QuienesSomos object', 1, '', 11, 1),
(14, '2014-12-03 22:27:09', '1', 'Producto object', 2, 'Modifica titulo_producto y descripcion_producto.', 7, 1),
(15, '2014-12-03 22:27:22', '2', 'Producto object', 1, '', 7, 1),
(16, '2014-12-03 22:27:36', '3', 'Producto object', 1, '', 7, 1),
(17, '2014-12-03 22:27:48', '4', 'Producto object', 1, '', 7, 1),
(18, '2014-12-05 18:34:44', '1', 'Foto object', 2, 'Modifica nombre_de_imagen.', 10, 1),
(19, '2014-12-05 18:46:52', '2', 'admin', 2, 'Modifica user_permissions.', 4, 1),
(20, '2014-12-05 18:47:20', '2', 'admin', 2, 'Modifica password.', 4, 1),
(21, '2014-12-05 18:56:38', '1', 'foto 1', 1, '', 10, 1),
(22, '2014-12-05 18:57:19', '1', 'foto 1', 2, 'Modifica imagen_original_slider.', 10, 1),
(23, '2014-12-05 18:59:55', '1', 'foto 1', 2, 'Modifica imagen_original_slider.', 10, 1),
(24, '2014-12-05 19:16:58', '1', 'Nosotros', 2, 'Modifica descripcion_nosotros.', 11, 1),
(25, '2014-12-05 19:17:32', '2', 'Nuestras delicias', 2, 'Modifica descripcion_nosotros y imagen_original_nosotros.', 11, 1),
(26, '2014-12-05 19:17:43', '1', 'Nosotros', 2, 'Modifica descripcion_nosotros y imagen_original_nosotros.', 11, 1),
(27, '2014-12-05 23:41:33', '2', 'Nuestras delicias', 3, '', 11, 1),
(28, '2014-12-05 23:43:26', '1', 'Nosotros', 2, 'Modifica descripcion_nosotros y imagen_original_nosotros.', 11, 1),
(29, '2014-12-05 23:55:50', '1', 'Nosotros', 2, 'No ha modificado ningún campo.', 11, 1),
(30, '2014-12-05 23:59:06', '1', 'Nosotros', 2, 'Modifica imagen_original_nosotros.', 11, 1),
(31, '2014-12-05 23:59:18', '1', 'Nosotros', 2, 'No ha modificado ningún campo.', 11, 1),
(32, '2014-12-05 23:59:28', '1', 'Nosotros', 2, 'Modifica imagen_original_nosotros.', 11, 1),
(33, '2014-12-06 00:00:48', '1', 'Nosotros', 2, 'Modifica imagen_original_nosotros.', 11, 1),
(34, '2014-12-06 00:01:09', '1', 'Nosotros', 2, 'Modifica imagen_original_nosotros.', 11, 1),
(35, '2014-12-09 16:23:23', '1', 'Nosotros', 2, 'No ha modificado ningún campo.', 11, 1),
(36, '2014-12-09 16:43:59', '1', 'Nosotros', 2, 'Modifica imagen_original_nosotros.', 11, 1),
(37, '2014-12-11 20:08:22', '1', 'Nosotros', 2, 'Modifica imagen_original_nosotros.', 11, 1),
(38, '2014-12-11 20:16:40', '1', 'Nosotros', 2, 'No ha modificado ningún campo.', 11, 1),
(39, '2014-12-11 20:16:51', '1', 'Nosotros', 2, 'Modifica imagen_original_nosotros.', 11, 1),
(40, '2014-12-11 20:16:59', '1', 'Nosotros', 2, 'Modifica imagen_original_nosotros.', 11, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=13 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'log entry', 'admin', 'logentry'),
(2, 'permission', 'auth', 'permission'),
(3, 'group', 'auth', 'group'),
(4, 'user', 'auth', 'user'),
(5, 'content type', 'contenttypes', 'contenttype'),
(6, 'session', 'sessions', 'session'),
(7, 'producto', 'productos', 'producto'),
(8, 'servicio', 'servicios', 'servicio'),
(9, 'imagen', 'servicios', 'imagen'),
(10, 'foto', 'sliderfotos', 'foto'),
(11, 'quienes somos', 'nosotros', 'quienessomos'),
(12, 'sitio', 'ajustes', 'sitio');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=36 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2014-10-03 21:55:41'),
(2, 'auth', '0001_initial', '2014-10-03 21:55:42'),
(3, 'admin', '0001_initial', '2014-10-03 21:55:43'),
(4, 'sessions', '0001_initial', '2014-10-03 21:55:43'),
(5, 'productos', '0001_initial', '2014-10-29 22:37:33'),
(6, 'productos', '0002_auto_20141104_2312', '2014-11-04 23:13:08'),
(7, 'servicios', '0001_initial', '2014-11-04 23:22:07'),
(8, 'servicios', '0002_imagen', '2014-11-05 21:34:48'),
(9, 'productos', '0003_auto_20141119_1953', '2014-11-19 20:01:03'),
(10, 'sliderfotos', '0001_initial', '2014-11-19 20:01:03'),
(11, 'nosotros', '0001_initial', '2014-11-19 21:29:03'),
(12, 'ajustes', '0001_initial', '2014-11-19 21:47:46'),
(13, 'servicios', '0003_auto_20141119_2201', '2014-11-19 22:01:18'),
(14, 'nosotros', '0002_auto_20141205_1454', '2014-12-05 17:55:24'),
(15, 'productos', '0004_auto_20141205_1454', '2014-12-05 17:55:24'),
(16, 'servicios', '0004_auto_20141205_1454', '2014-12-05 17:55:24'),
(17, 'sliderfotos', '0002_auto_20141205_1454', '2014-12-05 17:55:24'),
(18, 'nosotros', '0003_auto_20141205_1516', '2014-12-05 18:17:07'),
(19, 'productos', '0005_auto_20141205_1516', '2014-12-05 18:17:07'),
(20, 'servicios', '0005_auto_20141205_1516', '2014-12-05 18:17:07'),
(21, 'nosotros', '0004_auto_20141205_1519', '2014-12-05 18:19:25'),
(22, 'servicios', '0006_auto_20141205_1519', '2014-12-05 18:19:25'),
(23, 'ajustes', '0002_auto_20141205_1520', '2014-12-05 18:21:00'),
(24, 'sliderfotos', '0003_auto_20141205_1531', '2014-12-05 18:31:39'),
(25, 'sliderfotos', '0004_auto_20141205_1532', '2014-12-05 18:32:48'),
(26, 'sliderfotos', '0005_delete_foto', '2014-12-05 18:43:10'),
(27, 'sliderfotos', '0006_foto', '2014-12-05 18:53:47'),
(28, 'productos', '0006_auto_20141205_1559', '2014-12-05 18:59:07'),
(29, 'sliderfotos', '0007_auto_20141205_1559', '2014-12-05 18:59:07'),
(30, 'nosotros', '0005_auto_20141205_1601', '2014-12-05 19:01:43'),
(31, 'servicios', '0007_auto_20141205_1601', '2014-12-05 19:01:43'),
(32, 'ajustes', '0003_auto_20141205_1936', '2014-12-05 22:37:02'),
(33, 'nosotros', '0006_auto_20141205_1936', '2014-12-05 22:37:02'),
(34, 'nosotros', '0007_auto_20141205_2055', '2014-12-05 23:55:23'),
(35, 'nosotros', '0008_auto_20141205_2056', '2014-12-05 23:56:29');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('qsnv8otpimncpmc2dv7rr0ym9jntz2iy', 'NGYwZTc0OTcyYTVmNzEzZTdhZmE1Zjk1ZjkwNTZiOGEwMDE2NGU1NDp7Il9hdXRoX3VzZXJfaGFzaCI6IjllMjZmNGRlMDBmZWU3MjQ1MWQ1MzVlZThmMTE2NzlkYWQ0OGY5MmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2014-12-19 18:48:19'),
('siwt34r3os5vgnyywop9nnf2y4loman1', 'NGYwZTc0OTcyYTVmNzEzZTdhZmE1Zjk1ZjkwNTZiOGEwMDE2NGU1NDp7Il9hdXRoX3VzZXJfaGFzaCI6IjllMjZmNGRlMDBmZWU3MjQ1MWQ1MzVlZThmMTE2NzlkYWQ0OGY5MmIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9', '2014-11-12 21:11:12');

-- --------------------------------------------------------

--
-- Table structure for table `nosotros_quienessomos`
--

CREATE TABLE IF NOT EXISTS `nosotros_quienessomos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo_nosotros` varchar(100) NOT NULL,
  `descripcion_nosotros` longtext NOT NULL,
  `pub_date` time NOT NULL,
  `imagen_original_nosotros` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `nosotros_quienessomos`
--

INSERT INTO `nosotros_quienessomos` (`id`, `titulo_nosotros`, `descripcion_nosotros`, `pub_date`, `imagen_original_nosotros`) VALUES
(1, 'Nosotros', '<p>DULCE MARINA, SUS OR&Iacute;GENES</p>\r\n\r\n<p>Dulce Marina, reposter&iacute;a artesanal argentino &ndash; brasile&ntilde;a, como su nombre lo indica, somos una empresa destinada a la elaboraci&oacute;n de productos de pasteler&iacute;a y reposter&iacute;a profesional.</p>\r\n\r\n<p>Llevamos las tradiciones de la exquisita reposter&iacute;a argentina, como la de los originales sabores brasile&ntilde;os, utilizando materias primas de excelente calidad, recetas originales y elaboraci&oacute;n artesanal sin conservantes y colorantes.</p>\r\n\r\n<div>\r\n<p>Nuestros or&iacute;genes se remontan a principio del a&ntilde;o 2009 cuando, definitivamente instalados en Argentina, iniciamos el proyecto cargado de sue&ntilde;os y con la ambici&oacute;n de mostrar una faceta distinta a lo ya tradicionalmente conocido en Mendoza, aunque sin dejarlo de lado.</p>\r\n\r\n<p>Nuestra determinaci&oacute;n y perseverancia, unida a la calidad, originalidad y presentaci&oacute;n de nuestros productos nos llev&oacute; a la posibilidad de ofrecerte una amplia variedad exquisiteces, desde bombones del noroeste de Brasil o Cucas de la regi&oacute;n Sur hasta hermosas tortas de casamiento, pasando por tartas dulces y originales masitas que fusionan ambas tradiciones.</p>\r\n</div>\r\n', '17:16:59', 'nosotros/nosotros_xlSBDu3.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `productos_producto`
--

CREATE TABLE IF NOT EXISTS `productos_producto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo_producto` varchar(100) NOT NULL,
  `descripcion_producto` longtext,
  `pub_date` time,
  `imagen_original_producto` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `productos_producto`
--

INSERT INTO `productos_producto` (`id`, `titulo_producto`, `descripcion_producto`, `pub_date`, `imagen_original_producto`) VALUES
(1, 'Tartas', 'tartas', '22:27:09', '2014-12-05'),
(2, 'Tortas', 'tortas', '22:27:22', '2014-12-05'),
(3, 'Galletas', 'galletas', '22:27:36', '2014-12-05'),
(4, 'Alfajores', 'alfajores', '22:27:48', '2014-12-05');

-- --------------------------------------------------------

--
-- Table structure for table `servicios_imagen`
--

CREATE TABLE IF NOT EXISTS `servicios_imagen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `servicio_id` int(11) NOT NULL,
  `imagen_original` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `servicios_imagen_4bb699dc` (`servicio_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `servicios_imagen`
--

INSERT INTO `servicios_imagen` (`id`, `servicio_id`, `imagen_original`) VALUES
(1, 2, '2014-12-05'),
(2, 2, '2014-12-05');

-- --------------------------------------------------------

--
-- Table structure for table `servicios_servicio`
--

CREATE TABLE IF NOT EXISTS `servicios_servicio` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo_servicio` varchar(100) NOT NULL,
  `descripcion_servicio` longtext NOT NULL,
  `pub_date` time NOT NULL,
  `imagen_original_servicio` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `servicios_servicio`
--

INSERT INTO `servicios_servicio` (`id`, `titulo_servicio`, `descripcion_servicio`, `pub_date`, `imagen_original_servicio`) VALUES
(2, 'servicio de ejemplo', 'texto descriptivo del servicio de ejemplo', '22:16:38', '2014-12-05');

-- --------------------------------------------------------

--
-- Table structure for table `sliderfotos_foto`
--

CREATE TABLE IF NOT EXISTS `sliderfotos_foto` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre_de_imagen` varchar(50) NOT NULL,
  `imagen_original_slider` varchar(100) NOT NULL,
  `pub_date` time NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `sliderfotos_foto`
--

INSERT INTO `sliderfotos_foto` (`id`, `nombre_de_imagen`, `imagen_original_slider`, `pub_date`) VALUES
(1, 'foto 1', 'slider/img1.jpg', '15:59:55');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `servicios_imagen`
--
ALTER TABLE `servicios_imagen`
  ADD CONSTRAINT `servicios__servicio_id_7cf0e0fe8adb5c15_fk_servicios_servicio_id` FOREIGN KEY (`servicio_id`) REFERENCES `servicios_servicio` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
