-- phpMyAdmin SQL Dump
-- version 5.2.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Oct 29, 2025 at 01:03 PM
-- Server version: 8.4.3
-- PHP Version: 8.3.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `athletitrack_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `athletes_athlete`
--

CREATE TABLE `athletes_athlete` (
  `user_id` bigint NOT NULL,
  `birthday` date DEFAULT NULL,
  `medical_history` longtext,
  `contact_details` varchar(255) NOT NULL,
  `is_featured` tinyint(1) NOT NULL,
  `coach_id` bigint DEFAULT NULL,
  `team_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `athletes_athlete`
--

INSERT INTO `athletes_athlete` (`user_id`, `birthday`, `medical_history`, `contact_details`, `is_featured`, `coach_id`, `team_id`) VALUES
(8, NULL, NULL, '', 0, 3, 1),
(9, NULL, '', '09123456789', 0, 4, 3),
(10, NULL, NULL, '', 0, 6, 6),
(13, NULL, NULL, '', 0, 4, 3),
(14, NULL, NULL, '', 0, 7, 5);

-- --------------------------------------------------------

--
-- Table structure for table `athletes_performancestat`
--

CREATE TABLE `athletes_performancestat` (
  `id` bigint NOT NULL,
  `value` varchar(50) NOT NULL,
  `date_recorded` date NOT NULL,
  `athlete_id` bigint NOT NULL,
  `event_id` bigint DEFAULT NULL,
  `statistic_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `athletes_performancestat`
--

INSERT INTO `athletes_performancestat` (`id`, `value`, `date_recorded`, `athlete_id`, `event_id`, `statistic_id`) VALUES
(1, '1', '2025-08-25', 8, 1, 16),
(2, '1', '2025-08-25', 9, 2, 16),
(3, '1', '2025-08-25', 10, 3, 16),
(4, '60', '2025-08-26', 8, 1, 1),
(5, '60', '2025-08-26', 9, 2, 18),
(6, '25', '2025-08-26', 10, 3, 32),
(7, '5', '2025-10-16', 9, 2, 21);

-- --------------------------------------------------------

--
-- Table structure for table `audits_auditlog`
--

CREATE TABLE `audits_auditlog` (
  `id` bigint NOT NULL,
  `action` varchar(255) NOT NULL,
  `timestamp` datetime(6) NOT NULL,
  `details` longtext,
  `user_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

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
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add Scheduled task', 6, 'add_schedule'),
(22, 'Can change Scheduled task', 6, 'change_schedule'),
(23, 'Can delete Scheduled task', 6, 'delete_schedule'),
(24, 'Can view Scheduled task', 6, 'view_schedule'),
(25, 'Can add task', 7, 'add_task'),
(26, 'Can change task', 7, 'change_task'),
(27, 'Can delete task', 7, 'delete_task'),
(28, 'Can view task', 7, 'view_task'),
(29, 'Can add Failed task', 8, 'add_failure'),
(30, 'Can change Failed task', 8, 'change_failure'),
(31, 'Can delete Failed task', 8, 'delete_failure'),
(32, 'Can view Failed task', 8, 'view_failure'),
(33, 'Can add Successful task', 9, 'add_success'),
(34, 'Can change Successful task', 9, 'change_success'),
(35, 'Can delete Successful task', 9, 'delete_success'),
(36, 'Can view Successful task', 9, 'view_success'),
(37, 'Can add Queued task', 10, 'add_ormq'),
(38, 'Can change Queued task', 10, 'change_ormq'),
(39, 'Can delete Queued task', 10, 'delete_ormq'),
(40, 'Can view Queued task', 10, 'view_ormq'),
(41, 'Can add user', 11, 'add_customuser'),
(42, 'Can change user', 11, 'change_customuser'),
(43, 'Can delete user', 11, 'delete_customuser'),
(44, 'Can view user', 11, 'view_customuser'),
(45, 'Can add athlete', 12, 'add_athlete'),
(46, 'Can change athlete', 12, 'change_athlete'),
(47, 'Can delete athlete', 12, 'delete_athlete'),
(48, 'Can view athlete', 12, 'view_athlete'),
(49, 'Can add performance stat', 13, 'add_performancestat'),
(50, 'Can change performance stat', 13, 'change_performancestat'),
(51, 'Can delete performance stat', 13, 'delete_performancestat'),
(52, 'Can view performance stat', 13, 'view_performancestat'),
(53, 'Can add coach', 14, 'add_coach'),
(54, 'Can change coach', 14, 'change_coach'),
(55, 'Can delete coach', 14, 'delete_coach'),
(56, 'Can view coach', 14, 'view_coach'),
(57, 'Can add event', 15, 'add_event'),
(58, 'Can change event', 15, 'change_event'),
(59, 'Can delete event', 15, 'delete_event'),
(60, 'Can view event', 15, 'view_event'),
(61, 'Can add participation log', 16, 'add_participationlog'),
(62, 'Can change participation log', 16, 'change_participationlog'),
(63, 'Can delete participation log', 16, 'delete_participationlog'),
(64, 'Can view participation log', 16, 'view_participationlog'),
(65, 'Can add campus', 17, 'add_campus'),
(66, 'Can change campus', 17, 'change_campus'),
(67, 'Can delete campus', 17, 'delete_campus'),
(68, 'Can view campus', 17, 'view_campus'),
(69, 'Can add feedback', 18, 'add_feedback'),
(70, 'Can change feedback', 18, 'change_feedback'),
(71, 'Can delete feedback', 18, 'delete_feedback'),
(72, 'Can view feedback', 18, 'view_feedback'),
(73, 'Can add sport', 19, 'add_sport'),
(74, 'Can change sport', 19, 'change_sport'),
(75, 'Can delete sport', 19, 'delete_sport'),
(76, 'Can view sport', 19, 'view_sport'),
(77, 'Can add statistic', 20, 'add_statistic'),
(78, 'Can change statistic', 20, 'change_statistic'),
(79, 'Can delete statistic', 20, 'delete_statistic'),
(80, 'Can view statistic', 20, 'view_statistic'),
(81, 'Can add team', 21, 'add_team'),
(82, 'Can change team', 21, 'change_team'),
(83, 'Can delete team', 21, 'delete_team'),
(84, 'Can view team', 21, 'view_team'),
(85, 'Can add audit log', 22, 'add_auditlog'),
(86, 'Can change audit log', 22, 'change_auditlog'),
(87, 'Can delete audit log', 22, 'delete_auditlog'),
(88, 'Can view audit log', 22, 'view_auditlog');

-- --------------------------------------------------------

--
-- Table structure for table `coaches_coach`
--

CREATE TABLE `coaches_coach` (
  `user_id` bigint NOT NULL,
  `contact_number` varchar(20) NOT NULL,
  `team_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `coaches_coach`
--

INSERT INTO `coaches_coach` (`user_id`, `contact_number`, `team_id`) VALUES
(2, '09123456789', 2),
(3, '09123456789', 1),
(4, '09123456789', 3),
(5, '09123456789', 4),
(6, '09123456789', 6),
(7, '09123456789', 5);

-- --------------------------------------------------------

--
-- Table structure for table `core_campus`
--

CREATE TABLE `core_campus` (
  `id` bigint NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `core_campus`
--

INSERT INTO `core_campus` (`id`, `name`) VALUES
(1, 'Main Campus');

-- --------------------------------------------------------

--
-- Table structure for table `core_feedback`
--

CREATE TABLE `core_feedback` (
  `id` bigint NOT NULL,
  `sus_q1` int NOT NULL,
  `sus_q2` int NOT NULL,
  `sus_q3` int NOT NULL,
  `sus_q4` int NOT NULL,
  `sus_q5` int NOT NULL,
  `sus_q6` int NOT NULL,
  `sus_q7` int NOT NULL,
  `sus_q8` int NOT NULL,
  `sus_q9` int NOT NULL,
  `sus_q10` int NOT NULL,
  `comments` longtext,
  `submitted_at` datetime(6) NOT NULL,
  `user_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `core_sport`
--

CREATE TABLE `core_sport` (
  `id` bigint NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `core_sport`
--

INSERT INTO `core_sport` (`id`, `name`) VALUES
(1, '3x3 Basketball'),
(2, 'Basketball'),
(3, 'Volleyball');

-- --------------------------------------------------------

--
-- Table structure for table `core_statistic`
--

CREATE TABLE `core_statistic` (
  `id` bigint NOT NULL,
  `name` varchar(100) NOT NULL,
  `short_name` varchar(20) NOT NULL,
  `description` longtext,
  `sport_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `core_statistic`
--

INSERT INTO `core_statistic` (`id`, `name`, `short_name`, `description`, `sport_id`) VALUES
(1, 'PTS (Points)', 'pts', 'PTS (Points)', 1),
(3, 'Field Goals Made', 'FGM', 'Field Goals Made', 1),
(4, 'Field Goals Attempted', 'FGA', 'Field Goals Attempted', 1),
(5, '2-Point Made', '2PM', '2-Point Made', 1),
(6, '2-Point Attempted', '2PA', '2-Point Attempted', 1),
(7, 'Free Throws Made', 'FTM', 'Free Throws Made', 1),
(8, 'Free Throws Attempted', 'FTA', 'Free Throws Attempted', 1),
(9, 'Offensive Rebounds', 'OREB', 'Offensive Rebounds', 1),
(10, 'Defensive Rebounds', 'DREB', 'Defensive Rebounds', 1),
(11, 'Assists', 'AST', 'Assists', 1),
(12, 'Steals', 'STL', 'Steals', 1),
(13, 'Blocks', 'BLK', 'Blocks', 1),
(14, 'Turnovers', 'TO', 'Turnovers', 1),
(15, 'Personal Fouls', 'PF', 'Personal Fouls', 1),
(16, 'Wins', 'wins', NULL, NULL),
(17, 'Losses', 'losses', NULL, NULL),
(18, 'PTS (Points)', 'PTS', 'PTS (Points)', 2),
(19, 'Field Goals Made', 'FGM', 'Field Goals Made', 2),
(20, 'Field Goals Attempted', 'FGA', 'Field Goals Attempted', 2),
(21, '3-Point Made', '3PM', '3-Point Made', 2),
(22, '3-Point Attempted', '3PA', '3-Point Attempted', 2),
(23, 'Free Throws Made', 'FTM', 'Free Throws Made', 2),
(24, 'Free Throws Attempted', 'FTA', 'Free Throws Attempted', 2),
(25, 'Offensive Rebounds', 'OREB', 'Offensive Rebounds', 2),
(26, 'Defensive Rebounds', 'DREB', 'Defensive Rebounds', 2),
(27, 'AST (Assists)', 'AST', 'AST (Assists)', 2),
(28, 'STL (Steals)', 'STL', 'STL (Steals)', 2),
(29, 'BLK (Blocks)', 'BLK', 'BLK (Blocks)', 2),
(30, 'TO (Turnovers)', 'TO', 'TO (Turnovers)', 2),
(31, 'Personal Fouls', 'PF', 'Personal Fouls', 2),
(32, 'PTS (Points)', 'PTS', 'PTS (Points)', 3),
(33, 'K (Kills)', 'K', 'K (Kills)', 3),
(34, 'Attack Attempts', 'ATT', 'Attack Attempts', 3),
(35, 'DIG (Digs)', 'DIG', 'DIG (Digs)', 3),
(36, 'Reception', 'RE', 'Reception', 3),
(37, 'Assists, sometimes used for sets', 'AST', 'Assists, sometimes used for sets', 3),
(38, 'Blocks: Solo/Assist', 'BLK', 'Blocks: Solo/Assist', 3),
(39, 'Service Errors', 'SE', 'Service Errors', 3),
(40, 'Attack Errors', 'AE', 'Attack Errors', 3),
(41, 'Service Aces', 'SA', 'Service Aces', 3);

-- --------------------------------------------------------

--
-- Table structure for table `core_team`
--

CREATE TABLE `core_team` (
  `id` bigint NOT NULL,
  `gender` varchar(10) NOT NULL,
  `campus_id` bigint NOT NULL,
  `sport_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `core_team`
--

INSERT INTO `core_team` (`id`, `gender`, `campus_id`, `sport_id`) VALUES
(2, 'FEMALE', 1, 1),
(1, 'MALE', 1, 1),
(4, 'FEMALE', 1, 2),
(3, 'MALE', 1, 2),
(6, 'FEMALE', 1, 3),
(5, 'MALE', 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL
) ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2025-10-04 05:21:44.482272', '24', 'events.tasks.send_sms_reminders', 3, '', 6, 1),
(2, '2025-10-04 05:21:44.482604', '23', 'events.tasks.send_event_reminders', 3, '', 6, 1),
(3, '2025-10-04 05:21:44.482640', '22', 'events.tasks.send_sms_reminders', 3, '', 6, 1),
(4, '2025-10-04 05:21:44.482669', '21', 'events.tasks.send_event_reminders', 3, '', 6, 1),
(5, '2025-10-04 05:21:44.482696', '20', 'events.tasks.send_sms_reminders', 3, '', 6, 1),
(6, '2025-10-04 05:21:44.482723', '19', 'events.tasks.send_event_reminders', 3, '', 6, 1),
(7, '2025-10-04 05:21:44.482748', '7', 'events.tasks.send_event_reminders', 3, '', 6, 1),
(8, '2025-10-04 05:21:44.482772', '5', 'events.tasks.send_event_reminders', 3, '', 6, 1),
(9, '2025-10-04 05:21:44.482796', '3', 'events.tasks.send_event_reminders', 3, '', 6, 1),
(10, '2025-10-04 05:21:44.482819', '1', 'events.tasks.send_event_reminders', 3, '', 6, 1),
(11, '2025-10-04 05:21:44.482841', '8', 'events.tasks.send_sms_reminders', 3, '', 6, 1),
(12, '2025-10-04 05:21:44.482864', '6', 'events.tasks.send_sms_reminders', 3, '', 6, 1),
(13, '2025-10-04 05:21:44.482887', '4', 'events.tasks.send_sms_reminders', 3, '', 6, 1),
(14, '2025-10-04 05:21:44.482909', '2', 'events.tasks.send_sms_reminders', 3, '', 6, 1),
(15, '2025-10-04 05:21:44.482934', '18', 'events.tasks.send_sms_reminders', 3, '', 6, 1),
(16, '2025-10-04 05:21:44.482956', '17', 'events.tasks.send_event_reminders', 3, '', 6, 1),
(17, '2025-10-04 05:21:44.482978', '16', 'events.tasks.send_sms_reminders', 3, '', 6, 1),
(18, '2025-10-04 05:21:44.483001', '15', 'events.tasks.send_event_reminders', 3, '', 6, 1),
(19, '2025-10-04 05:21:44.483022', '14', 'events.tasks.send_sms_reminders', 3, '', 6, 1),
(20, '2025-10-04 05:21:44.483044', '13', 'events.tasks.send_event_reminders', 3, '', 6, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(12, 'athletes', 'athlete'),
(13, 'athletes', 'performancestat'),
(22, 'audits', 'auditlog'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(14, 'coaches', 'coach'),
(4, 'contenttypes', 'contenttype'),
(17, 'core', 'campus'),
(18, 'core', 'feedback'),
(19, 'core', 'sport'),
(20, 'core', 'statistic'),
(21, 'core', 'team'),
(8, 'django_q', 'failure'),
(10, 'django_q', 'ormq'),
(6, 'django_q', 'schedule'),
(9, 'django_q', 'success'),
(7, 'django_q', 'task'),
(15, 'events', 'event'),
(16, 'events', 'participationlog'),
(5, 'sessions', 'session'),
(11, 'users', 'customuser');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2025-08-25 06:18:09.401799'),
(2, 'contenttypes', '0002_remove_content_type_name', '2025-08-25 06:18:09.525110'),
(3, 'auth', '0001_initial', '2025-08-25 06:18:09.959840'),
(4, 'auth', '0002_alter_permission_name_max_length', '2025-08-25 06:18:10.049618'),
(5, 'auth', '0003_alter_user_email_max_length', '2025-08-25 06:18:10.058760'),
(6, 'auth', '0004_alter_user_username_opts', '2025-08-25 06:18:10.067525'),
(7, 'auth', '0005_alter_user_last_login_null', '2025-08-25 06:18:10.079550'),
(8, 'auth', '0006_require_contenttypes_0002', '2025-08-25 06:18:10.084223'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2025-08-25 06:18:10.092822'),
(10, 'auth', '0008_alter_user_username_max_length', '2025-08-25 06:18:10.101947'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2025-08-25 06:18:10.110817'),
(12, 'auth', '0010_alter_group_name_max_length', '2025-08-25 06:18:10.136414'),
(13, 'auth', '0011_update_proxy_permissions', '2025-08-25 06:18:10.153156'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2025-08-25 06:18:10.161137'),
(15, 'users', '0001_initial', '2025-08-25 06:18:10.649419'),
(16, 'admin', '0001_initial', '2025-08-25 06:18:10.882247'),
(17, 'admin', '0002_logentry_remove_auto_add', '2025-08-25 06:18:10.892349'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2025-08-25 06:18:10.907807'),
(19, 'events', '0001_initial', '2025-08-25 06:18:10.965696'),
(20, 'core', '0001_initial', '2025-08-25 06:18:11.124722'),
(21, 'core', '0002_initial', '2025-08-25 06:18:11.523985'),
(22, 'coaches', '0001_initial', '2025-08-25 06:18:11.770466'),
(23, 'athletes', '0001_initial', '2025-08-25 06:18:12.384755'),
(24, 'audits', '0001_initial', '2025-08-25 06:18:12.411640'),
(25, 'audits', '0002_initial', '2025-08-25 06:18:12.518879'),
(26, 'django_q', '0001_initial', '2025-08-25 06:18:12.579780'),
(27, 'django_q', '0002_auto_20150630_1624', '2025-08-25 06:18:12.721398'),
(28, 'django_q', '0003_auto_20150708_1326', '2025-08-25 06:18:12.848441'),
(29, 'django_q', '0004_auto_20150710_1043', '2025-08-25 06:18:12.857593'),
(30, 'django_q', '0005_auto_20150718_1506', '2025-08-25 06:18:12.991426'),
(31, 'django_q', '0006_auto_20150805_1817', '2025-08-25 06:18:13.067680'),
(32, 'django_q', '0007_ormq', '2025-08-25 06:18:13.099893'),
(33, 'django_q', '0008_auto_20160224_1026', '2025-08-25 06:18:13.106746'),
(34, 'django_q', '0009_auto_20171009_0915', '2025-08-25 06:18:13.179765'),
(35, 'django_q', '0010_auto_20200610_0856', '2025-08-25 06:18:13.192602'),
(36, 'django_q', '0011_auto_20200628_1055', '2025-08-25 06:18:13.221760'),
(37, 'django_q', '0012_auto_20200702_1608', '2025-08-25 06:18:13.228398'),
(38, 'django_q', '0013_task_attempt_count', '2025-08-25 06:18:13.268232'),
(39, 'django_q', '0014_schedule_cluster', '2025-08-25 06:18:13.292172'),
(40, 'django_q', '0015_alter_schedule_schedule_type', '2025-08-25 06:18:13.323591'),
(41, 'django_q', '0016_schedule_intended_date_kwarg', '2025-08-25 06:18:13.376745'),
(42, 'django_q', '0017_task_cluster_alter', '2025-08-25 06:18:13.427785'),
(43, 'django_q', '0018_task_success_index', '2025-08-25 06:18:13.457790'),
(44, 'events', '0002_initial', '2025-08-25 06:18:13.768484'),
(45, 'sessions', '0001_initial', '2025-08-25 06:18:13.823039');

-- --------------------------------------------------------

--
-- Table structure for table `django_q_ormq`
--

CREATE TABLE `django_q_ormq` (
  `id` int NOT NULL,
  `key` varchar(100) NOT NULL,
  `payload` longtext NOT NULL,
  `lock` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_q_schedule`
--

CREATE TABLE `django_q_schedule` (
  `id` int NOT NULL,
  `func` varchar(256) NOT NULL,
  `hook` varchar(256) DEFAULT NULL,
  `args` longtext,
  `kwargs` longtext,
  `schedule_type` varchar(2) NOT NULL,
  `repeats` int NOT NULL,
  `next_run` datetime(6) DEFAULT NULL,
  `task` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `minutes` smallint UNSIGNED DEFAULT NULL,
  `cron` varchar(100) DEFAULT NULL,
  `cluster` varchar(100) DEFAULT NULL,
  `intended_date_kwarg` varchar(100) DEFAULT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_q_task`
--

CREATE TABLE `django_q_task` (
  `name` varchar(100) NOT NULL,
  `func` varchar(256) NOT NULL,
  `hook` varchar(256) DEFAULT NULL,
  `args` longtext,
  `kwargs` longtext,
  `result` longtext,
  `started` datetime(6) NOT NULL,
  `stopped` datetime(6) NOT NULL,
  `success` tinyint(1) NOT NULL,
  `id` varchar(32) NOT NULL,
  `group` varchar(100) DEFAULT NULL,
  `attempt_count` int NOT NULL,
  `cluster` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_q_task`
--

INSERT INTO `django_q_task` (`name`, `func`, `hook`, `args`, `kwargs`, `result`, `started`, `stopped`, `success`, `id`, `group`, `attempt_count`, `cluster`) VALUES
('spring-summer-north-neptune', 'events.tasks.send_event_reminders', NULL, 'gAWVBQAAAAAAAABLEIWULg==', 'gAV9lC4=', NULL, '2025-10-28 13:19:02.607228', '2025-10-28 13:19:08.323719', 1, '031c11dcbca04a8087c6825d5c0fb77c', 'event_email_reminder_16', 1, 'athletitrack_cluster'),
('wolfram-mobile-venus-may', 'events.tasks.send_event_reminders', NULL, 'gAWVBQAAAAAAAABLC4WULg==', 'gAV9lC4=', NULL, '2025-10-04 05:29:02.111132', '2025-10-04 05:29:03.350654', 1, '2fb4b0d2a5ab4acb995680a474be0f42', NULL, 1, 'athletitrack_cluster'),
('lake-harry-comet-pip', 'events.tasks.send_event_reminders', NULL, 'gAWVBQAAAAAAAABLDIWULg==', 'gAV9lC4=', NULL, '2025-10-16 12:45:42.314313', '2025-10-16 12:45:43.335134', 1, '665517518880491bac94809360e2331e', NULL, 1, 'athletitrack_cluster'),
('stairway-alabama-golf-delaware', 'events.tasks.send_event_reminders', NULL, 'gAWVBQAAAAAAAABLC4WULg==', 'gAV9lC4=', NULL, '2025-10-16 12:44:18.291979', '2025-10-16 12:44:45.944322', 1, '6d223fa344064a09ad225b81b2d986dc', NULL, 1, 'athletitrack_cluster'),
('queen-thirteen-triple-solar', 'events.tasks.send_event_reminders', NULL, 'gAWVBQAAAAAAAABLGIWULg==', 'gAV9lC4=', NULL, '2025-10-04 05:20:58.810926', '2025-10-04 05:21:01.967096', 1, 'ac18cac8a6c440fca762ab8f392bc418', NULL, 1, 'athletitrack_cluster'),
('mirror-artist-wolfram-pizza', 'events.tasks.send_event_reminders', NULL, 'gAWVBQAAAAAAAABLAYWULg==', 'gAV9lC4=', NULL, '2025-10-04 04:33:47.427845', '2025-10-04 04:33:50.804114', 1, 'afa5d650d57346eaa167605fd98a42a1', NULL, 1, 'athletitrack_cluster'),
('stream-kilo-avocado-lion', 'events.tasks.send_event_reminders', NULL, 'gAWVBQAAAAAAAABLEYWULg==', 'gAV9lC4=', NULL, '2025-10-28 13:35:13.796929', '2025-10-28 13:35:16.414349', 1, 'c7397d56b9ad4b2e9425de6024795c7b', 'event_email_reminder_17', 1, 'athletitrack_cluster'),
('johnny-echo-ack-enemy', 'events.tasks.send_event_reminders', NULL, 'gAWVBQAAAAAAAABLDYWULg==', 'gAV9lC4=', NULL, '2025-10-16 12:45:57.776884', '2025-10-16 12:45:58.638301', 1, 'da30be3fc4944d2493bfb5996534adc3', NULL, 1, 'athletitrack_cluster'),
('cardinal-triple-batman-venus', 'events.tasks.send_event_reminders', NULL, 'gAWVBQAAAAAAAABLGYWULg==', 'gAV9lC4=', NULL, '2025-10-04 05:27:05.359585', '2025-10-04 05:27:06.352061', 1, 'e39d9fc1f0154246b5462ccd69d1f1a2', NULL, 1, 'athletitrack_cluster');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0hr4psj442hmu65fpdxziyst91xay4g8', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1vE22X:yidFZ9ZvNBdmSV6uVigvKVuFxy7J2nZL2JZ8ruraCQc', '2025-10-29 11:00:21.201029'),
('0j15dt1emc3g5ycuu0kl05fnbzqdpu18', '.eJxVjDsOwjAQBe_iGln2-rempOcM1vqHA8iR4qRC3B0ipYD2zcx7sUDb2sI2yhKmzM7Ms9PvFik9St9BvlO_zTzNfV2myHeFH3Tw65zL83K4fweNRvvWCAZRIxkA5UwBYcFpcloZoZPQ0SuIqWZZwFtJhKpag1ZW752KMiX2_gChNDaR:1vE26c:IzQSyS8-kxdFPCeSsJ1yerWA6ucha9nRuqgde-7zKNU', '2025-10-29 11:04:34.415862'),
('0po9qshmq1ox3cdnx5wvgpkq8zv30geu', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v4sh1:pDPc9QxroOjacJclkg3VJkDGVYIvxNYFBcufmdgDnAM', '2025-10-04 05:12:19.463266'),
('1ev0u0eynzfye8b38lh0qpqez6mo8x8g', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1vDkJv:RJ_TBWj0QVlF8D2nhIQ6ecp50nhwsZ25zMiCRjbwFSY', '2025-10-28 16:05:07.205282'),
('267h9xfpwk3edtdtf0a1zmily52r8edb', '.eJxVjDsOwjAQBe_iGln2-rempOcM1vqHA8iR4qRC3B0ipYD2zcx7sUDb2sI2yhKmzM7Ms9PvFik9St9BvlO_zTzNfV2myHeFH3Tw65zL83K4fweNRvvWCAZRIxkA5UwBYcFpcloZoZPQ0SuIqWZZwFtJhKpag1ZW752KMiX2_gChNDaR:1v9biI:6WmeEl-PduVToXL67CkEFYQl9k8lQx0YXmAjpdyyZyo', '2025-10-17 06:05:10.084868'),
('3t8tks9em4sgwyoci0r6rbgfsj1e78o1', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1uqQYd:FmI5GeFScehvTjQRKSyP1cJSFk_X6z_uqYxjm6YdjQ4', '2025-08-25 08:19:55.117480'),
('4v0m546bca1v8ighznpdjr52abg1ddzd', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v9EFj:hwAM8Vxtx_KBMzlLoqm8NYwd0ygdejOlMkuU9YdkNrE', '2025-10-16 05:02:07.556182'),
('7j3kl9n8wg49tpue1h2z1jomadozduc4', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v9IUG:vchJ6j4TQFcsMCy89E6a2ejpQFP0dWh1CGl3hlZ0s8Q', '2025-10-16 09:33:24.320057'),
('7muf1jsirywzlc2rd7p0jce14cmqikee', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v9EKG:-Mv_yq5yowwpS-XXfQCnEzOMIfQUJqH23B6RYPsSiq8', '2025-10-16 05:06:48.031397'),
('aspzjqphkr7cxbt9xlbj3geklen1ggsx', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1vA4dC:tebcf3no_wq3ShFCK0DZLsIPqIbTJhne-3vQru7Pigg', '2025-10-18 12:57:50.025559'),
('aznprqtdisa6o3m7vfqhbcomj10ha4dw', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v4uaN:ZsAgH57XaIi9B4ktEb_IVlIXGoBqJpPvpzg_Giy0FfI', '2025-10-04 07:13:35.053066'),
('b8eilkg3bft3jbnf8s4r7saozsinel1g', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1uqubL:hXsO5nd5mrrG380g7v8xeVUv5ZvhopCPXXStXKSPkNo', '2025-08-26 16:24:43.349348'),
('c52lutxb8klv4d1zx9ozome5i1tz21s2', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1vE1fR:pe_INKvleCKZiCN1Y6404kyN928FuJnkvg5uQWkKAZo', '2025-10-29 10:36:29.575298'),
('cvsnp5zqftx38khp8g4i5bwgvokkav8p', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v0Cu3:aCGSbjCsTYsPTh7IBeV6YALkvbMxhCAJDSzl5KjKW_Q', '2025-09-21 07:46:27.101686'),
('d8st2964ouekovt7tctdmpwhlmqh8qs3', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1urCzu:EGmpe7sczUM4wNe_OGhSY38NutqvHjAiLU4SEGLcUW0', '2025-08-27 12:03:18.338548'),
('f656ejkxa904ggufkzpd5lt4nug11g0c', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1uwBDh:FauyBZeSYZ6nhsnOx3GlLDDJsdj3aPr5zW4cPqcmCG4', '2025-09-10 05:10:05.865612'),
('fs9kvzb3kunwu4iirav8irrrma6mf780', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v9N83:Z0EgX6035AoUo9umwLOL3BKd51q3-yJ0-wgOs48puZQ', '2025-10-16 14:30:47.847251'),
('h47ipfqp5n0vxvxqyq9py7ur1p89pgfd', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1vE23x:VKrvPPwwZ77wvsna9ef2YqmQlJuAgdJwLeNSVOFEqw4', '2025-10-29 11:01:49.912969'),
('hmgwyrsasmkosivuln0ftvaigskp1wbz', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1uu0F4:x-anjGnKQpYsRsJSzuuwipgTYLQMfCZx_Rp8ZGpYZLo', '2025-09-04 05:02:30.283625'),
('htigaob74f9f99ld3zv4hb4ew5n8l6ie', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v9EWm:OB10V7xSmMWTAdeZmw4-m-Yc8oPb3xtjfacdWwIg6HY', '2025-10-16 05:19:44.013053'),
('i1zu0927blywvppnnnm9q942qn7x6pby', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1vDkEk:EVfFcCeBJ-B7Y05lvEtfCdsZRVxiD_kEV4y7l3O5Nqg', '2025-10-28 15:59:46.567618'),
('i27wpg4takuobktop0vgujzgy3ixth1h', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1uz64l:kTd5WdSUtyfUuuqdDfH2PmjiFMoEsr7H47fvKb0U7uQ', '2025-09-18 06:16:55.448376'),
('ihhu6x53vrnimqw596c7v3fx8mf2srp2', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1uyhSq:cg7h1zO_z2Bk1PDHKhVb-iH5rPXnT0f0cy_F8zTVXLg', '2025-09-17 04:00:08.151281'),
('k8w88ehx3uqfa47y12lbef2uh3axdp8p', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1vDkHJ:U0pcpMY5usqzceTU-kCymASRuHVXsXLtHPwhDfDw2L8', '2025-10-28 16:02:25.789520'),
('ln2t6bymmlmgnkpf6j8jnjopmeoi2ih3', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1uyYC1:KNHZP3yuemSL_Vlu_oq_OaMg5Ph6WyhUXvqm1nwNrYE', '2025-09-16 18:06:09.689447'),
('ngka40wxxn02k3n0s2vwrh39bzcqvfqb', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v9J3r:PW8NyJH47Jh2OVDAQ4ci-JGCInEMytFlKUzDxi5zt14', '2025-10-16 10:10:11.489743'),
('ppbwabdiowwvfvzefh6tbx5zgamjpvct', '.eJxVjDsOwjAQBe_iGln2-rempOcM1vqHA8iR4qRC3B0ipYD2zcx7sUDb2sI2yhKmzM7Ms9PvFik9St9BvlO_zTzNfV2myHeFH3Tw65zL83K4fweNRvvWCAZRIxkA5UwBYcFpcloZoZPQ0SuIqWZZwFtJhKpag1ZW752KMiX2_gChNDaR:1v9Zal:o2aNtyO8fJrlav3GR-bAs6Mv96hyWd7aqAG7Zb8DcFk', '2025-10-17 03:49:15.177601'),
('qivud1ia8fe3cv1v14rwk6o4mt8glyhx', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v92xZ:Q8LHrLiPDMgjg4L17ahurLVIpvp8Sh45_sl1Z5f6tOg', '2025-10-15 16:58:37.940537'),
('r7by8ngm4mpuj76bqqaylg0l1tipo93z', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v908D:h2NDhuftHf8s5inmXTWgTf86NdacgPPIoBxAmauNjog', '2025-10-15 13:57:25.833879'),
('rvp4ne9sqlv80v71hav4gcywp3moshyq', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1vDkCs:vEZTnImg10eQjBDphgJV_ykg-WQyacc4MyyHG3wNdwI', '2025-10-28 15:57:50.702165'),
('snhi30fnjvkwhdrwviwxa0mr6292k9fr', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v4qbM:Y3ApKdMTRyxL84DutXtrNbHhvGFBaHcIVYxs7cNyoBc', '2025-10-04 02:58:20.567717'),
('t7izocqutssynxc51ob4e9z83b0zxlue', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v93qe:kORgBO0O2IuuH37hJROjQrtwaKbrot6yDSNHewyu63U', '2025-10-15 17:55:32.089423'),
('taba3ukr8k9c4zi7zou693u8jj1wzgn8', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v9GSD:sCHgslKqZ3VwuvRy_yMpI48lc-x_NQKtF4MnhJsQtDg', '2025-10-16 07:23:09.646854'),
('tix8ki57gxgq2fjjw78t7rarvs10rr1j', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v4waG:konyeFRgzo09UWFN52u54Egn2NXMcSZO2FMqIKe7ZVM', '2025-10-04 09:21:36.268501'),
('tn7in80tn3h0wwctgdcqdcr8zszwtjnn', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1vDjVx:qcl65kIFEwS9PiJqT7Y39OeR0qkQeJ5rSljAqExz1Wk', '2025-10-28 15:13:29.857393'),
('tp5idxuhal0dks5bkdjkeyktscdbqx0s', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1uwhcA:M1Do5H2nf4rlgJSQiVhAT6hFFFXeOksdE_zn_p8jwLQ', '2025-09-11 15:45:30.822417'),
('tpqy5p494u0awd3x4wlgry4d5nit1sr0', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1vBC2L:toF_V0fjcu9Rxlt-OpZOlIuXkumxGtOS6GMxypLYCdU', '2025-10-21 15:04:25.651731'),
('ttwolm0ea0lcwr1fwy35b5y3mb9uyotr', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v0eoI:TyuDt0pjeA74g8HDJgDZ9Aq80TfREks0frHLvjmP4g4', '2025-09-22 13:34:22.681634'),
('ua0x8j8m1wjjsknnsb1iql593wj7thwi', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1vDeuR:42VKyTL1Ye2dHECe65mNDMMdoQMDvbW0awYhOZiIj44', '2025-10-28 10:18:27.672187'),
('ud5wjjbn3ta734zb7hpcav98gs3ud17y', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v0AzD:cqtxF1PrlUgQBBw9f3NfoS3XF6y6vFTQZ-9hC1UQugc', '2025-09-21 05:43:39.261943'),
('ysew8spj39k7hr4exi5psgy1ej8kseyo', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v9bho:6Jz4p462R9QyWM1bR7EykurLnOGRtxzjsyfl0eOcj-I', '2025-10-17 06:04:40.560851'),
('yw0dqf95l4tnhni054d4o7rhmmcq6ymi', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v0gmv:-jUdHblQi08aN3u6FM-E53aElDSnNczXWZmVAmCzQqk', '2025-09-22 15:41:05.543371'),
('z061leqt2qjcmltbt4f47phtg7lkbhmq', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v9G5F:HSTigxqC9h94t5u_YD4u8WCP9EajX4ev1UNmn-ZC6wo', '2025-10-16 06:59:25.677158'),
('zozfumpbszhnoxo2z7v0y9j9qbzzcs25', '.eJxVjMsOwiAQAP-FsyGF5VE8eu83kIXdStXQpLQn478bkh70OjOZt4h47CUejbe4kLgKJS6_LGF-cu2CHljvq8xr3bclyZ7I0zY5rcSv29n-DQq20rfGGQ6gsp85WICgWduUDDhQxgaNqCGMw-iRjAaPs3eUGZQfOAM4Ep8vtH425g:1v9ETV:DtNJD0Pr1_nfR1qfL4I9MficgDE94-OiYoSDinfxmw8', '2025-10-16 05:16:21.287347');

-- --------------------------------------------------------

--
-- Table structure for table `events_event`
--

CREATE TABLE `events_event` (
  `id` bigint NOT NULL,
  `name` varchar(200) NOT NULL,
  `description` longtext NOT NULL,
  `start_time` datetime(6) NOT NULL,
  `end_time` datetime(6) NOT NULL,
  `location` varchar(255) NOT NULL,
  `our_score` int DEFAULT NULL,
  `opponent_score` int DEFAULT NULL,
  `coach_in_charge_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `events_event`
--

INSERT INTO `events_event` (`id`, `name`, `description`, `start_time`, `end_time`, `location`, `our_score`, `opponent_score`, `coach_in_charge_id`) VALUES
(1, '3 x 3', 'test', '2025-08-25 06:37:00.000000', '2025-08-25 08:37:00.000000', 'tac', 60, 40, 3),
(2, 'E vs U', 'test', '2025-08-25 06:45:00.000000', '2025-08-25 07:45:00.000000', 'tac', 60, 40, 4),
(3, 'E vs U', 'test', '2025-08-25 06:45:00.000000', '2025-08-25 08:45:00.000000', 'tac', 25, 15, 6),
(17, '1 testing only', 'test', '2025-10-28 13:36:00.000000', '2025-10-28 13:44:00.000000', 'tac', NULL, NULL, 7);

-- --------------------------------------------------------

--
-- Table structure for table `events_participationlog`
--

CREATE TABLE `events_participationlog` (
  `id` bigint NOT NULL,
  `status` varchar(10) NOT NULL,
  `notes` longtext,
  `athlete_id` bigint NOT NULL,
  `event_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `events_participationlog`
--

INSERT INTO `events_participationlog` (`id`, `status`, `notes`, `athlete_id`, `event_id`) VALUES
(1, 'REGISTERED', NULL, 8, 1),
(2, 'REGISTERED', NULL, 9, 2),
(3, 'REGISTERED', NULL, 10, 3),
(28, 'REGISTERED', NULL, 14, 17);

-- --------------------------------------------------------

--
-- Table structure for table `users_customuser`
--

CREATE TABLE `users_customuser` (
  `id` bigint NOT NULL,
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
  `role` varchar(50) NOT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users_customuser`
--

INSERT INTO `users_customuser` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `role`, `gender`, `birthday`, `image`) VALUES
(1, 'pbkdf2_sha256$1000000$8h2NsIJV6qtxYWBi96JKS5$2eKJV1mfbUmF1QnQTbNSgcHgMUaEUiiE8gP2dmqfLTA=', '2025-10-29 09:01:49.896253', 1, 'admin', '', '', 'admin@admin.com', 1, 1, '2025-08-25 06:19:24.686968', 'ADMINISTRATOR', NULL, NULL, ''),
(2, 'pbkdf2_sha256$1000000$PJF9ugf0ZTyqaPOVF8VtO2$gXT3tuqXmGmqkleGjKKjsqjHDTkVS8nhZgyZafvnjnA=', NULL, 0, 'jenny.doe', 'jenny', 'doe', 'jennydoe@email.com', 0, 1, '2025-08-25 06:23:43.307207', 'COACH', NULL, NULL, ''),
(3, 'pbkdf2_sha256$1000000$ZlDSr26u9mDZztWiDagc5R$dzwIYTjFMoRu2VJ2B7LidfiDIa/q49Jaa5Pss6wVjFQ=', NULL, 0, 'terrence.romeo', 'terrence', 'Romeo', 'terrence@email.com', 0, 1, '2025-08-25 06:23:56.213846', 'COACH', NULL, NULL, ''),
(4, 'pbkdf2_sha256$1000000$7lZe96CmzsOFOM75csIxUV$zZdrP6vIavFXM0JmVm4NUSn4W79MgTnEwSDsFE8YXfY=', NULL, 0, 'basketball.boys', 'basketball', 'boys', 'basketballboys@gmail.com', 0, 1, '2025-08-25 06:24:16.165183', 'COACH', 'MALE', NULL, ''),
(5, 'pbkdf2_sha256$1000000$SfZDyhwbaDhyQ7Gx9pSV1i$dhncYjrvDVh5eUd/ESIYaPpy8rKBhcJeg5O0bErEHgA=', NULL, 0, 'basketball.girls', 'basketball', 'girls', 'basketballgirls@gmail.com', 0, 1, '2025-08-25 06:24:28.826450', 'COACH', NULL, NULL, ''),
(6, 'pbkdf2_sha256$1000000$LgecxGrvQMeJqQz69FkwRK$7doUnFjo6cNnaazdgabmpj4+U/Ka8oskF1dR+iPXwbQ=', '2025-08-26 14:24:20.480646', 0, 'jane.doe', 'Jane', 'Doe', 'janedoe@email.com', 0, 1, '2025-08-25 06:24:45.824566', 'COACH', 'FEMALE', NULL, ''),
(7, 'pbkdf2_sha256$1000000$eHzY4C8p5U6dEShrJgzAqL$S8wbsmUD7e37sKwgfi0kHaq/tbNINJT/YKLlKLUiZFY=', NULL, 0, 'john.doe', 'john', 'doe', 'johndoe@email.com', 0, 1, '2025-08-25 06:25:00.879744', 'COACH', NULL, NULL, ''),
(8, 'pbkdf2_sha256$1000000$X1SY6WY4bDtT2JDSERpuxS$S3jngzhk9vubCDS6JkdUeb+8EyTyJsrvYlqMxMGh5yE=', NULL, 0, 'lebron.james', 'Lebron', 'James', 'lebronjames@gmail.com', 0, 1, '2025-08-25 06:25:21.925325', 'ATHLETE', 'MALE', NULL, ''),
(9, 'pbkdf2_sha256$1000000$q2ceM6LUBdTzFV9BqTYNFC$2Bujp03Ag+yQRLnd+wlGJHrYdDdDwE2lXJGGb+QLVzs=', '2025-10-29 09:04:34.396922', 0, 'kang.kong', 'kang', 'kong', 'kangkong@gmail.com', 0, 1, '2025-08-25 06:25:36.268945', 'ATHLETE', 'MALE', '2003-08-11', 'profile_images/a21d12a3930f06351b6e982da94fcec5_1.jpg'),
(10, 'pbkdf2_sha256$1000000$VbEGCsHSUavUpuoXarr4tE$eocgBYsBGtK+4Ld6vNixDdqjL8l3Ts0OGiQw4jRb8lA=', NULL, 0, 'alyssa.garcia', 'Alyssa', 'Garcia', 'alyssa.g@evsu.edu.ph', 0, 1, '2025-08-25 06:44:34.788637', 'ATHLETE', 'FEMALE', NULL, ''),
(11, 'pbkdf2_sha256$1000000$jW1w8RT22Tz4bWxLoJdvyI$2lUjXtISHkeJbUAeiah8x91PskVWYcgu3jhfbhyqdyk=', NULL, 0, 'john patrick.camposano', 'John Patrick', 'Camposano', 'johnpatrick.camposano@evsu.edu.ph', 0, 1, '2025-10-04 03:39:49.361240', 'ATHLETE', 'MALE', NULL, ''),
(12, 'pbkdf2_sha256$1000000$ziu07Han2Pk4GwnaCrrGJn$hHk6wePmhpZdWGnSQPGtoHlDv69/gFfB7X2sRdpVSBw=', NULL, 0, 'john patrick a.camposano', 'John Patrick A', 'Camposano', 'johnpatrickcamposano@gmail.com', 0, 1, '2025-10-04 04:12:20.511093', 'ATHLETE', 'MALE', NULL, ''),
(13, 'pbkdf2_sha256$1000000$iAVG5Sydj738DXzvGdalIk$2UdRHt0+2tqOwVuS4bAIhuHAeu8qA2QeaqIhHB46OgQ=', '2025-10-15 14:21:44.904330', 0, 'jaypee.tinaya', 'Jaypee', 'Tinaya', 'jaypee.tinaya@evsu.edu.ph', 0, 1, '2025-10-15 11:58:41.712029', 'ATHLETE', 'MALE', NULL, ''),
(14, 'pbkdf2_sha256$1000000$wZQyhMvFXgp6ZUULiOdLWb$zAqQP4UIKG58XVY0ARHTaoya4EjCSxWwGD/WdjryBuQ=', NULL, 0, 'anthonio.macasa', 'Anthonio', 'Macasa', 'antoniojr.macasa@evsu.edu.ph', 0, 1, '2025-10-15 11:59:31.112363', 'ATHLETE', 'MALE', NULL, '');

-- --------------------------------------------------------

--
-- Table structure for table `users_customuser_groups`
--

CREATE TABLE `users_customuser_groups` (
  `id` bigint NOT NULL,
  `customuser_id` bigint NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_customuser_user_permissions`
--

CREATE TABLE `users_customuser_user_permissions` (
  `id` bigint NOT NULL,
  `customuser_id` bigint NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `athletes_athlete`
--
ALTER TABLE `athletes_athlete`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `athletes_athlete_coach_id_a1832ef9_fk_coaches_coach_user_id` (`coach_id`),
  ADD KEY `athletes_athlete_team_id_79fb6e8f_fk_core_team_id` (`team_id`);

--
-- Indexes for table `athletes_performancestat`
--
ALTER TABLE `athletes_performancestat`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `athletes_performancestat_athlete_id_statistic_id__944394da_uniq` (`athlete_id`,`statistic_id`,`event_id`),
  ADD KEY `athletes_performancestat_event_id_bf810950_fk_events_event_id` (`event_id`),
  ADD KEY `athletes_performance_statistic_id_2f8e193a_fk_core_stat` (`statistic_id`);

--
-- Indexes for table `audits_auditlog`
--
ALTER TABLE `audits_auditlog`
  ADD PRIMARY KEY (`id`),
  ADD KEY `audits_auditlog_user_id_b8884964_fk_users_customuser_id` (`user_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `coaches_coach`
--
ALTER TABLE `coaches_coach`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `team_id` (`team_id`);

--
-- Indexes for table `core_campus`
--
ALTER TABLE `core_campus`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `core_feedback`
--
ALTER TABLE `core_feedback`
  ADD PRIMARY KEY (`id`),
  ADD KEY `core_feedback_user_id_630c6a53_fk_users_customuser_id` (`user_id`);

--
-- Indexes for table `core_sport`
--
ALTER TABLE `core_sport`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `core_statistic`
--
ALTER TABLE `core_statistic`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `core_statistic_sport_id_short_name_01fb03e6_uniq` (`sport_id`,`short_name`);

--
-- Indexes for table `core_team`
--
ALTER TABLE `core_team`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `core_team_sport_id_campus_id_gender_d11002c6_uniq` (`sport_id`,`campus_id`,`gender`),
  ADD KEY `core_team_campus_id_727f9be6_fk_core_campus_id` (`campus_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_users_customuser_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_q_ormq`
--
ALTER TABLE `django_q_ormq`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_q_schedule`
--
ALTER TABLE `django_q_schedule`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_q_task`
--
ALTER TABLE `django_q_task`
  ADD PRIMARY KEY (`id`),
  ADD KEY `success_index` (`group`,`name`,`func`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `events_event`
--
ALTER TABLE `events_event`
  ADD PRIMARY KEY (`id`),
  ADD KEY `events_event_coach_in_charge_id_59ec0497_fk_coaches_c` (`coach_in_charge_id`);

--
-- Indexes for table `events_participationlog`
--
ALTER TABLE `events_participationlog`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `events_participationlog_event_id_athlete_id_fb152403_uniq` (`event_id`,`athlete_id`),
  ADD KEY `events_participation_athlete_id_5e56a2f5_fk_athletes_` (`athlete_id`);

--
-- Indexes for table `users_customuser`
--
ALTER TABLE `users_customuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `users_customuser_groups`
--
ALTER TABLE `users_customuser_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_customuser_groups_customuser_id_group_id_76b619e3_uniq` (`customuser_id`,`group_id`),
  ADD KEY `users_customuser_groups_group_id_01390b14_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `users_customuser_user_permissions`
--
ALTER TABLE `users_customuser_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `users_customuser_user_pe_customuser_id_permission_7a7debf6_uniq` (`customuser_id`,`permission_id`),
  ADD KEY `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` (`permission_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `athletes_performancestat`
--
ALTER TABLE `athletes_performancestat`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `audits_auditlog`
--
ALTER TABLE `audits_auditlog`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=89;

--
-- AUTO_INCREMENT for table `core_campus`
--
ALTER TABLE `core_campus`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `core_feedback`
--
ALTER TABLE `core_feedback`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `core_sport`
--
ALTER TABLE `core_sport`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `core_statistic`
--
ALTER TABLE `core_statistic`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `core_team`
--
ALTER TABLE `core_team`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT for table `django_q_ormq`
--
ALTER TABLE `django_q_ormq`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `django_q_schedule`
--
ALTER TABLE `django_q_schedule`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `events_event`
--
ALTER TABLE `events_event`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT for table `events_participationlog`
--
ALTER TABLE `events_participationlog`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT for table `users_customuser`
--
ALTER TABLE `users_customuser`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `users_customuser_groups`
--
ALTER TABLE `users_customuser_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `users_customuser_user_permissions`
--
ALTER TABLE `users_customuser_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `athletes_athlete`
--
ALTER TABLE `athletes_athlete`
  ADD CONSTRAINT `athletes_athlete_coach_id_a1832ef9_fk_coaches_coach_user_id` FOREIGN KEY (`coach_id`) REFERENCES `coaches_coach` (`user_id`),
  ADD CONSTRAINT `athletes_athlete_team_id_79fb6e8f_fk_core_team_id` FOREIGN KEY (`team_id`) REFERENCES `core_team` (`id`),
  ADD CONSTRAINT `athletes_athlete_user_id_602f8b28_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`);

--
-- Constraints for table `athletes_performancestat`
--
ALTER TABLE `athletes_performancestat`
  ADD CONSTRAINT `athletes_performance_athlete_id_bf7f9be5_fk_athletes_` FOREIGN KEY (`athlete_id`) REFERENCES `athletes_athlete` (`user_id`),
  ADD CONSTRAINT `athletes_performance_statistic_id_2f8e193a_fk_core_stat` FOREIGN KEY (`statistic_id`) REFERENCES `core_statistic` (`id`),
  ADD CONSTRAINT `athletes_performancestat_event_id_bf810950_fk_events_event_id` FOREIGN KEY (`event_id`) REFERENCES `events_event` (`id`);

--
-- Constraints for table `audits_auditlog`
--
ALTER TABLE `audits_auditlog`
  ADD CONSTRAINT `audits_auditlog_user_id_b8884964_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `coaches_coach`
--
ALTER TABLE `coaches_coach`
  ADD CONSTRAINT `coaches_coach_team_id_5ef88c79_fk_core_team_id` FOREIGN KEY (`team_id`) REFERENCES `core_team` (`id`),
  ADD CONSTRAINT `coaches_coach_user_id_f15609bb_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`);

--
-- Constraints for table `core_feedback`
--
ALTER TABLE `core_feedback`
  ADD CONSTRAINT `core_feedback_user_id_630c6a53_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`);

--
-- Constraints for table `core_statistic`
--
ALTER TABLE `core_statistic`
  ADD CONSTRAINT `core_statistic_sport_id_e4068ff2_fk_core_sport_id` FOREIGN KEY (`sport_id`) REFERENCES `core_sport` (`id`);

--
-- Constraints for table `core_team`
--
ALTER TABLE `core_team`
  ADD CONSTRAINT `core_team_campus_id_727f9be6_fk_core_campus_id` FOREIGN KEY (`campus_id`) REFERENCES `core_campus` (`id`),
  ADD CONSTRAINT `core_team_sport_id_c03ae432_fk_core_sport_id` FOREIGN KEY (`sport_id`) REFERENCES `core_sport` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_customuser_id` FOREIGN KEY (`user_id`) REFERENCES `users_customuser` (`id`);

--
-- Constraints for table `events_event`
--
ALTER TABLE `events_event`
  ADD CONSTRAINT `events_event_coach_in_charge_id_59ec0497_fk_coaches_c` FOREIGN KEY (`coach_in_charge_id`) REFERENCES `coaches_coach` (`user_id`);

--
-- Constraints for table `events_participationlog`
--
ALTER TABLE `events_participationlog`
  ADD CONSTRAINT `events_participation_athlete_id_5e56a2f5_fk_athletes_` FOREIGN KEY (`athlete_id`) REFERENCES `athletes_athlete` (`user_id`),
  ADD CONSTRAINT `events_participationlog_event_id_9d92cc57_fk_events_event_id` FOREIGN KEY (`event_id`) REFERENCES `events_event` (`id`);

--
-- Constraints for table `users_customuser_groups`
--
ALTER TABLE `users_customuser_groups`
  ADD CONSTRAINT `users_customuser_gro_customuser_id_958147bf_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `users_customuser` (`id`),
  ADD CONSTRAINT `users_customuser_groups_group_id_01390b14_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `users_customuser_user_permissions`
--
ALTER TABLE `users_customuser_user_permissions`
  ADD CONSTRAINT `users_customuser_use_customuser_id_5771478b_fk_users_cus` FOREIGN KEY (`customuser_id`) REFERENCES `users_customuser` (`id`),
  ADD CONSTRAINT `users_customuser_use_permission_id_baaa2f74_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
