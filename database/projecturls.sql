-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Nov 22, 2023 at 10:47 AM
-- Server version: 10.4.10-MariaDB
-- PHP Version: 7.3.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `projecturls`
--
CREATE DATABASE IF NOT EXISTS `projecturls` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `projecturls`;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`)
) ENGINE=MyISAM AUTO_INCREMENT=89 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add user model', 7, 'add_usermodel'),
(26, 'Can change user model', 7, 'change_usermodel'),
(27, 'Can delete user model', 7, 'delete_usermodel'),
(28, 'Can view user model', 7, 'view_usermodel'),
(29, 'Can add dataset', 8, 'add_dataset'),
(30, 'Can change dataset', 8, 'change_dataset'),
(31, 'Can delete dataset', 8, 'delete_dataset'),
(32, 'Can view dataset', 8, 'view_dataset'),
(33, 'Can add test model', 9, 'add_testmodel'),
(34, 'Can change test model', 9, 'change_testmodel'),
(35, 'Can delete test model', 9, 'delete_testmodel'),
(36, 'Can view test model', 9, 'view_testmodel'),
(37, 'Can add urlm odel', 10, 'add_urlmodel'),
(38, 'Can change urlm odel', 10, 'change_urlmodel'),
(39, 'Can delete urlm odel', 10, 'delete_urlmodel'),
(40, 'Can view urlm odel', 10, 'view_urlmodel'),
(41, 'Can add last_login', 11, 'add_last_login'),
(42, 'Can change last_login', 11, 'change_last_login'),
(43, 'Can delete last_login', 11, 'delete_last_login'),
(44, 'Can view last_login', 11, 'view_last_login'),
(45, 'Can add ad a_algo', 12, 'add_ada_algo'),
(46, 'Can change ad a_algo', 12, 'change_ada_algo'),
(47, 'Can delete ad a_algo', 12, 'delete_ada_algo'),
(48, 'Can view ad a_algo', 12, 'view_ada_algo'),
(49, 'Can add d t_algo', 13, 'add_dt_algo'),
(50, 'Can change d t_algo', 13, 'change_dt_algo'),
(51, 'Can delete d t_algo', 13, 'delete_dt_algo'),
(52, 'Can view d t_algo', 13, 'view_dt_algo'),
(53, 'Can add kn n_algo', 14, 'add_knn_algo'),
(54, 'Can change kn n_algo', 14, 'change_knn_algo'),
(55, 'Can delete kn n_algo', 14, 'delete_knn_algo'),
(56, 'Can view kn n_algo', 14, 'view_knn_algo'),
(57, 'Can add linear_al go', 15, 'add_linear_algo'),
(58, 'Can change linear_al go', 15, 'change_linear_algo'),
(59, 'Can delete linear_al go', 15, 'delete_linear_algo'),
(60, 'Can view linear_al go', 15, 'view_linear_algo'),
(61, 'Can add random forest', 16, 'add_randomforest'),
(62, 'Can change random forest', 16, 'change_randomforest'),
(63, 'Can delete random forest', 16, 'delete_randomforest'),
(64, 'Can view random forest', 16, 'view_randomforest'),
(65, 'Can add sx m_algo', 17, 'add_sxm_algo'),
(66, 'Can change sx m_algo', 17, 'change_sxm_algo'),
(67, 'Can delete sx m_algo', 17, 'delete_sxm_algo'),
(68, 'Can view sx m_algo', 17, 'view_sxm_algo'),
(69, 'Can add x g_algo', 18, 'add_xg_algo'),
(70, 'Can change x g_algo', 18, 'change_xg_algo'),
(71, 'Can delete x g_algo', 18, 'delete_xg_algo'),
(72, 'Can view x g_algo', 18, 'view_xg_algo'),
(73, 'Can add sv r_algo', 17, 'add_svr_algo'),
(74, 'Can change sv r_algo', 17, 'change_svr_algo'),
(75, 'Can delete sv r_algo', 17, 'delete_svr_algo'),
(76, 'Can view sv r_algo', 17, 'view_svr_algo'),
(77, 'Can add sv m_algo', 17, 'add_svm_algo'),
(78, 'Can change sv m_algo', 17, 'change_svm_algo'),
(79, 'Can delete sv m_algo', 17, 'delete_svm_algo'),
(80, 'Can view sv m_algo', 17, 'view_svm_algo'),
(81, 'Can add random forest_al go', 16, 'add_randomforest_algo'),
(82, 'Can change random forest_al go', 16, 'change_randomforest_algo'),
(83, 'Can delete random forest_al go', 16, 'delete_randomforest_algo'),
(84, 'Can view random forest_al go', 16, 'view_randomforest_algo'),
(85, 'Can add logistic_al go', 15, 'add_logistic_algo'),
(86, 'Can change logistic_al go', 15, 'change_logistic_algo'),
(87, 'Can delete logistic_al go', 15, 'delete_logistic_algo'),
(88, 'Can view logistic_al go', 15, 'view_logistic_algo');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  KEY `auth_user_groups_group_id_97559544` (`group_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `dataset`
--

DROP TABLE IF EXISTS `dataset`;
CREATE TABLE IF NOT EXISTS `dataset` (
  `data_id` int(11) NOT NULL AUTO_INCREMENT,
  `data_set` varchar(100) NOT NULL,
  `Accuracy` double DEFAULT NULL,
  `F1_Score` double DEFAULT NULL,
  `Precision` double DEFAULT NULL,
  `Recall` double DEFAULT NULL,
  `algo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`data_id`)
) ENGINE=MyISAM AUTO_INCREMENT=49 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dataset`
--

INSERT INTO `dataset` (`data_id`, `data_set`, `Accuracy`, `F1_Score`, `Precision`, `Recall`, `algo`) VALUES
(48, 'files/url_10k_0zk1a0o.csv', 0.9815, 0.9814999953749988, 0.9816994130849646, 0.9817133855117401, 'SVM'),
(47, 'files/url_10k_mv1etRQ.csv', 0.987, 0.9869989469147, 0.9870674652231837, 0.9869797916766668, 'Random Forest');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6` (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=MyISAM AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'mainapp', 'usermodel'),
(8, 'adminapp', 'dataset'),
(9, 'userapp', 'testmodel'),
(10, 'userapp', 'urlmodel'),
(11, 'mainapp', 'last_login'),
(12, 'adminapp', 'ada_algo'),
(13, 'adminapp', 'dt_algo'),
(14, 'adminapp', 'knn_algo'),
(15, 'adminapp', 'logistic_algo'),
(16, 'adminapp', 'randomforest_algo'),
(17, 'adminapp', 'svm_algo'),
(18, 'adminapp', 'xg_algo');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2023-11-01 06:06:22.327637'),
(2, 'auth', '0001_initial', '2023-11-01 06:06:22.889860'),
(3, 'admin', '0001_initial', '2023-11-01 06:06:23.048477'),
(4, 'admin', '0002_logentry_remove_auto_add', '2023-11-01 06:06:23.064099'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2023-11-01 06:06:23.080245'),
(6, 'adminapp', '0001_initial', '2023-11-01 06:06:23.112983'),
(7, 'contenttypes', '0002_remove_content_type_name', '2023-11-01 06:06:23.235737'),
(8, 'auth', '0002_alter_permission_name_max_length', '2023-11-01 06:06:23.310163'),
(9, 'auth', '0003_alter_user_email_max_length', '2023-11-01 06:06:23.386686'),
(10, 'auth', '0004_alter_user_username_opts', '2023-11-01 06:06:23.402676'),
(11, 'auth', '0005_alter_user_last_login_null', '2023-11-01 06:06:23.481878'),
(12, 'auth', '0006_require_contenttypes_0002', '2023-11-01 06:06:23.481878'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2023-11-01 06:06:23.501292'),
(14, 'auth', '0008_alter_user_username_max_length', '2023-11-01 06:06:23.746726'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2023-11-01 06:06:23.909225'),
(16, 'auth', '0010_alter_group_name_max_length', '2023-11-01 06:06:23.970080'),
(17, 'auth', '0011_update_proxy_permissions', '2023-11-01 06:06:23.982298'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2023-11-01 06:06:24.078477'),
(19, 'mainapp', '0001_initial', '2023-11-01 06:06:24.117352'),
(20, 'sessions', '0001_initial', '2023-11-01 06:06:24.181243'),
(21, 'userapp', '0001_initial', '2023-11-01 06:06:24.284513'),
(22, 'mainapp', '0002_last_login_usermodel_date_time_and_more', '2023-11-01 10:35:07.515559'),
(23, 'mainapp', '0003_rename_otp_num_usermodel_otp', '2023-11-02 08:59:19.539607'),
(24, 'mainapp', '0004_rename_otp_usermodel_otp_num', '2023-11-02 09:11:09.437293'),
(25, 'mainapp', '0005_remove_usermodel_user_dob_usermodel_user_age', '2023-11-02 10:05:40.765794'),
(26, 'userapp', '0002_urlmodel_user_qrcode', '2023-11-07 05:34:16.999824'),
(27, 'adminapp', '0002_ada_algo_dt_algo_knn_algo_linear_algo_randomforest_and_more', '2023-11-07 07:47:33.845832'),
(28, 'adminapp', '0003_rename_sxm_algo_svr_algo_alter_linear_algo_table_and_more', '2023-11-07 07:50:39.718361'),
(29, 'adminapp', '0004_rename_xg_id_ada_algo_ada_id_and_more', '2023-11-07 08:01:55.587777'),
(30, 'adminapp', '0005_rename_svr_algo_svm_algo_delete_ada_algo_and_more', '2023-11-07 08:20:41.128724'),
(31, 'adminapp', '0006_rename_randomforest_randomforest_algo', '2023-11-07 08:34:18.521644'),
(32, 'adminapp', '0007_remove_dataset_accuracy_remove_dataset_f1_score_and_more', '2023-11-07 08:48:30.663111'),
(33, 'adminapp', '0008_rename_linear_algo_logistic_algo_and_more', '2023-11-07 09:04:00.643407'),
(34, 'adminapp', '0009_dataset_accuracy_dataset_f1_score_dataset_precision_and_more', '2023-11-07 09:34:38.741852');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('quk0b1cy0n8ayl2ofumwbc9635aulej1', 'eyJ1c2VyX2lkIjoyMywidXNlcl9lbWFpbCI6InByYXNoYW50aGkzNzY2QGdtYWlsLmNvbSJ9:1qys0j:5Ahycq959Dk4FYINlUzxyr9JRwenjVKxkYT99Wdi4A0', '2023-11-17 11:06:45.532367'),
('efybcncy3915w90inocxq74rnqt3avsm', 'eyJ1c2VyX2lkIjoyM30:1qzyni:Aimqb4oinp7ZO-wjEGczI4L0d4DJuq_RjSt2gliSSkA', '2023-11-20 12:33:54.175145'),
('06jh92tx3r1xny8q0l8mf0gwe6vcewjr', 'eyJ1c2VyX2lkIjoyM30:1r0KfS:qVBOq3fGXnJn5Gjf1kI6zGbf11ou9uq_FxwjmWgdjbI', '2023-11-21 11:54:50.018049');

-- --------------------------------------------------------

--
-- Table structure for table `knn_algo`
--

DROP TABLE IF EXISTS `knn_algo`;
CREATE TABLE IF NOT EXISTS `knn_algo` (
  `KNN_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Accuracy` double DEFAULT NULL,
  `F1_Score` double DEFAULT NULL,
  `Precision` double DEFAULT NULL,
  `Recall` double DEFAULT NULL,
  `algo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`KNN_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `last_login`
--

DROP TABLE IF EXISTS `last_login`;
CREATE TABLE IF NOT EXISTS `last_login` (
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Login_Time` datetime(6) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `logistic`
--

DROP TABLE IF EXISTS `logistic`;
CREATE TABLE IF NOT EXISTS `logistic` (
  `Logistic_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Accuracy` double DEFAULT NULL,
  `F1_Score` double DEFAULT NULL,
  `Precision` double DEFAULT NULL,
  `Recall` double DEFAULT NULL,
  `algo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Logistic_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `randomforest`
--

DROP TABLE IF EXISTS `randomforest`;
CREATE TABLE IF NOT EXISTS `randomforest` (
  `Random_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Accuracy` double DEFAULT NULL,
  `F1_Score` double DEFAULT NULL,
  `Precision` double DEFAULT NULL,
  `Recall` double DEFAULT NULL,
  `algo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Random_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `svm_algo`
--

DROP TABLE IF EXISTS `svm_algo`;
CREATE TABLE IF NOT EXISTS `svm_algo` (
  `SVR_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Accuracy` double DEFAULT NULL,
  `F1_Score` double DEFAULT NULL,
  `Precision` double DEFAULT NULL,
  `Recall` double DEFAULT NULL,
  `algo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`SVR_ID`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `testing_details`
--

DROP TABLE IF EXISTS `testing_details`;
CREATE TABLE IF NOT EXISTS `testing_details` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `testurl` longtext NOT NULL,
  `test_qrcode` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `url_qr_details`
--

DROP TABLE IF EXISTS `url_qr_details`;
CREATE TABLE IF NOT EXISTS `url_qr_details` (
  `url_id` int(11) NOT NULL AUTO_INCREMENT,
  `url` longtext NOT NULL,
  `user_url_id` int(11) NOT NULL,
  `user_qrcode` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`url_id`),
  KEY `URL_QR_Details_user_url_id_dc4e9d7a` (`user_url_id`)
) ENGINE=MyISAM AUTO_INCREMENT=50 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `url_qr_details`
--

INSERT INTO `url_qr_details` (`url_id`, `url`, `user_url_id`, `user_qrcode`) VALUES
(1, '', 23, NULL),
(2, '', 23, NULL),
(3, 'diaryofagameaddict.com', 23, NULL),
(4, 'toddscarwash.com', 23, NULL),
(5, 'toddscarwash.com', 23, 'qrcodes/image951.png'),
(6, 'toddscarwash.com', 23, 'qrcodes/image844.png'),
(7, 'diaryofagameaddict.com', 23, ''),
(8, 'diaryofagameaddict.com', 23, ''),
(9, 'diaryofagameaddict.com', 23, ''),
(10, 'toddscarwash.com', 23, ''),
(11, 'toddscarwash.com', 23, ''),
(12, 'diaryofagameaddict.com', 23, ''),
(13, 'toddscarwash.com', 23, ''),
(14, 'toddscarwash.com', 23, ''),
(15, '', 23, ''),
(16, 'toddscarwash.com', 23, ''),
(17, 'toddscarwash.com', 23, ''),
(18, 'toddscarwash.com', 23, ''),
(19, 'toddscarwash.com', 23, ''),
(20, 'toddscarwash.com', 23, ''),
(21, 'diaryofagameaddict.com', 23, ''),
(22, 'diaryofagameaddict.com', 23, ''),
(23, 'diaryofagameaddict.com', 23, ''),
(24, 'diaryofagameaddict.com', 23, ''),
(25, 'toddscarwash.com', 23, ''),
(26, 'toddscarwash.com', 23, ''),
(27, 'toddscarwash.com', 23, ''),
(28, 'diaryofagameaddict.com', 23, ''),
(29, 'toddscarwash.com', 23, ''),
(30, 'diaryofagameaddict.com', 23, ''),
(31, 'albany.craigslist.org/reb/2687304936.html', 23, ''),
(32, 'toddscarwash.com', 23, ''),
(33, 'toddscarwash.com', 23, ''),
(34, 'diaryofagameaddict.com', 23, ''),
(35, 'diaryofagameaddict.com', 23, ''),
(36, 'diaryofagameaddict.com', 23, ''),
(37, 'diaryofagameaddict.com', 23, ''),
(38, 'diaryofagameaddict.com', 23, ''),
(39, 'toddscarwash.com', 23, ''),
(40, 'diaryofagameaddict.com', 23, ''),
(41, 'toddscarwash.com', 23, ''),
(42, 'toddscarwash.com', 23, ''),
(43, 'toddscarwash.com', 23, ''),
(44, 'toddscarwash.com', 23, ''),
(45, 'toddscarwash.com', 23, ''),
(46, 'diaryofagameaddict.com', 23, ''),
(47, 'diaryofagameaddict.com', 23, ''),
(48, 'diaryofagameaddict.com', 23, ''),
(49, 'diaryofagameaddict.com', 23, '');

-- --------------------------------------------------------

--
-- Table structure for table `user_details`
--

DROP TABLE IF EXISTS `user_details`;
CREATE TABLE IF NOT EXISTS `user_details` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) NOT NULL,
  `user_email` varchar(254) NOT NULL,
  `user_password` varchar(50) NOT NULL,
  `user_address` longtext NOT NULL,
  `user_contact` varchar(15) NOT NULL,
  `user_image` varchar(100) DEFAULT NULL,
  `Date_Time` datetime(6) DEFAULT NULL,
  `Last_Login_Date` date DEFAULT NULL,
  `Last_Login_Time` time(6) DEFAULT NULL,
  `Message` longtext DEFAULT NULL,
  `No_Of_Times_Login` int(11) DEFAULT NULL,
  `Otp_Num` int(11) DEFAULT NULL,
  `Otp_Status` longtext DEFAULT NULL,
  `User_Status` longtext DEFAULT NULL,
  `user_age` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `user_details`
--

INSERT INTO `user_details` (`user_id`, `user_name`, `user_email`, `user_password`, `user_address`, `user_contact`, `user_image`, `Date_Time`, `Last_Login_Date`, `Last_Login_Time`, `Message`, `No_Of_Times_Login`, `Otp_Num`, `Otp_Status`, `User_Status`, `user_age`) VALUES
(23, 'prashanthii', 'pprashanthi169@gmail.com', 'Amma@123', 'Hyderabad', '9949803766', 'media/rose_Y6vn3sN.jpg', '2023-11-07 11:54:50.009071', '2023-11-02', '15:39:19.493379', 'Good', 15, 2658, 'verified', 'accepted', 25);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
