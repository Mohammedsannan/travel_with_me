/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.22 : Database - travel
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`travel` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `travel`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=81 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add login',7,'add_login'),
(26,'Can change login',7,'change_login'),
(27,'Can delete login',7,'delete_login'),
(28,'Can view login',7,'view_login'),
(29,'Can add resorts',8,'add_resorts'),
(30,'Can change resorts',8,'change_resorts'),
(31,'Can delete resorts',8,'delete_resorts'),
(32,'Can view resorts',8,'view_resorts'),
(33,'Can add restaurant',9,'add_restaurant'),
(34,'Can change restaurant',9,'change_restaurant'),
(35,'Can delete restaurant',9,'delete_restaurant'),
(36,'Can view restaurant',9,'view_restaurant'),
(37,'Can add touristplace',10,'add_touristplace'),
(38,'Can change touristplace',10,'change_touristplace'),
(39,'Can delete touristplace',10,'delete_touristplace'),
(40,'Can view touristplace',10,'view_touristplace'),
(41,'Can add userregistration',11,'add_userregistration'),
(42,'Can change userregistration',11,'change_userregistration'),
(43,'Can delete userregistration',11,'delete_userregistration'),
(44,'Can view userregistration',11,'view_userregistration'),
(45,'Can add touristplacereviewrating',12,'add_touristplacereviewrating'),
(46,'Can change touristplacereviewrating',12,'change_touristplacereviewrating'),
(47,'Can delete touristplacereviewrating',12,'delete_touristplacereviewrating'),
(48,'Can view touristplacereviewrating',12,'view_touristplacereviewrating'),
(49,'Can add restaurantreviewrating',13,'add_restaurantreviewrating'),
(50,'Can change restaurantreviewrating',13,'change_restaurantreviewrating'),
(51,'Can delete restaurantreviewrating',13,'delete_restaurantreviewrating'),
(52,'Can view restaurantreviewrating',13,'view_restaurantreviewrating'),
(53,'Can add restaurantfacility',14,'add_restaurantfacility'),
(54,'Can change restaurantfacility',14,'change_restaurantfacility'),
(55,'Can delete restaurantfacility',14,'delete_restaurantfacility'),
(56,'Can view restaurantfacility',14,'view_restaurantfacility'),
(57,'Can add resortroom',15,'add_resortroom'),
(58,'Can change resortroom',15,'change_resortroom'),
(59,'Can delete resortroom',15,'delete_resortroom'),
(60,'Can view resortroom',15,'view_resortroom'),
(61,'Can add resortreviewrating',16,'add_resortreviewrating'),
(62,'Can change resortreviewrating',16,'change_resortreviewrating'),
(63,'Can delete resortreviewrating',16,'delete_resortreviewrating'),
(64,'Can view resortreviewrating',16,'view_resortreviewrating'),
(65,'Can add resortfacility',17,'add_resortfacility'),
(66,'Can change resortfacility',17,'change_resortfacility'),
(67,'Can delete resortfacility',17,'delete_resortfacility'),
(68,'Can view resortfacility',17,'view_resortfacility'),
(69,'Can add fooditem',18,'add_fooditem'),
(70,'Can change fooditem',18,'change_fooditem'),
(71,'Can delete fooditem',18,'delete_fooditem'),
(72,'Can view fooditem',18,'view_fooditem'),
(73,'Can add feedback',19,'add_feedback'),
(74,'Can change feedback',19,'change_feedback'),
(75,'Can delete feedback',19,'delete_feedback'),
(76,'Can view feedback',19,'view_feedback'),
(77,'Can add complaints',20,'add_complaints'),
(78,'Can change complaints',20,'change_complaints'),
(79,'Can delete complaints',20,'delete_complaints'),
(80,'Can view complaints',20,'view_complaints');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session'),
(20,'travel_planning','complaints'),
(19,'travel_planning','feedback'),
(18,'travel_planning','fooditem'),
(7,'travel_planning','login'),
(17,'travel_planning','resortfacility'),
(16,'travel_planning','resortreviewrating'),
(15,'travel_planning','resortroom'),
(8,'travel_planning','resorts'),
(9,'travel_planning','restaurant'),
(14,'travel_planning','restaurantfacility'),
(13,'travel_planning','restaurantreviewrating'),
(10,'travel_planning','touristplace'),
(12,'travel_planning','touristplacereviewrating'),
(11,'travel_planning','userregistration');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-03-24 05:31:44.889525'),
(2,'auth','0001_initial','2023-03-24 05:31:46.002755'),
(3,'admin','0001_initial','2023-03-24 05:31:46.242999'),
(4,'admin','0002_logentry_remove_auto_add','2023-03-24 05:31:46.256047'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-03-24 05:31:46.267076'),
(6,'contenttypes','0002_remove_content_type_name','2023-03-24 05:31:46.432733'),
(7,'auth','0002_alter_permission_name_max_length','2023-03-24 05:31:46.526505'),
(8,'auth','0003_alter_user_email_max_length','2023-03-24 05:31:46.557110'),
(9,'auth','0004_alter_user_username_opts','2023-03-24 05:31:46.566976'),
(10,'auth','0005_alter_user_last_login_null','2023-03-24 05:31:46.648099'),
(11,'auth','0006_require_contenttypes_0002','2023-03-24 05:31:46.655539'),
(12,'auth','0007_alter_validators_add_error_messages','2023-03-24 05:31:46.665215'),
(13,'auth','0008_alter_user_username_max_length','2023-03-24 05:31:46.764315'),
(14,'auth','0009_alter_user_last_name_max_length','2023-03-24 05:31:46.891468'),
(15,'auth','0010_alter_group_name_max_length','2023-03-24 05:31:46.936657'),
(16,'auth','0011_update_proxy_permissions','2023-03-24 05:31:46.959631'),
(17,'auth','0012_alter_user_first_name_max_length','2023-03-24 05:31:47.231052'),
(18,'sessions','0001_initial','2023-03-24 05:31:47.299395'),
(19,'travel_planning','0001_initial','2023-03-24 05:31:49.459139'),
(20,'travel_planning','0002_alter_touristplacereviewrating_tpid','2023-04-11 04:36:18.883588'),
(21,'travel_planning','0003_complaints','2023-05-04 06:43:14.752612'),
(22,'travel_planning','0004_auto_20230505_1123','2023-05-05 05:54:23.198844');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('3xnavp0erqmwjmkflpz5bbeco2migteu','eyJsaWQiOjEwLCJybWlkIjoxfQ:1pkJW5:wyMdOiieshXPeAFicvhm-TnwZSrdFWItXRNTgjlVf6k','2023-04-20 06:54:41.486468'),
('4g0n5i6zdh3ymp952l1fjdz175z6umwy','eyJsb2NpZCI6NCwibGlkIjoyMCwidHBpZCI6MSwic25hbWUiOiJNaXJhY2xlIFJlc29ydHMifQ:1poNXO:o4wm_VVlKbpKSyKauLgvdtwzb3jIWC-eFVWwsfL-uwo','2023-05-01 12:00:50.748267'),
('cbnyryyfjrzot7ynm2rwwblx6udc8shg','eyJsaWQiOjcsInNuYW1lIjoiUGFyYWdvbiBSZXN0YXVyYW50IiwiZmRpZCI6MX0:1pofN7:XlSz8LP_6YFV2G5haLj97liy1BPrsh1WP-Ku5Bu4idg','2023-05-02 07:03:25.313443'),
('ik52bqu4o1hi8a341h3pscdsebk5grz5','eyJsb2NpZCI6MywidHBpZCI6M30:1plndJ:fo9I8yKgvZxybufTim-f45ozFerlaPxjtpYBqS7rWRk','2023-04-24 09:16:17.825535'),
('k2jpzkm54a2yh3duikge23nneiqxlmei','eyJ0cGlkIjoxLCJsb2NpZCI6NH0:1poeit:LnB63_IYYSmFtkpRtjaSKyDkM_wC66KWJ-6KyRX666g','2023-05-02 06:21:51.337679'),
('mun01j7houwgrd68cb0g8x52fubmglgi','eyJsaWQiOjl9:1pg1RR:stcVf5wPIRRWYzwzlQDj2qM9iCf9Q1FaITubsBADJ2A','2023-04-08 10:48:09.645828'),
('po25mh5xu7cbns5abv5upkeejusqxt3m','.eJyrVsrJT85MUbIy01EqKQAxDHWUcsC0uY5ScV5ibqqSlZJPqoJzYl5KTmqxQlBqcX5RiYKSjlJyfi5EQy0A19oVMg:1pupFB:6cibUFJ6cns92Lywup4MZH-xQb6pHiO9atG778yeomQ','2023-05-19 06:48:41.350798'),
('urqasr5ev0mlvpiitqbg57t8kxirncrx','eyJsaWQiOjcsInNuYW1lIjoiUGFyYWdvbiBSZXN0YXVyYW50IiwiZmRpZCI6MX0:1poeyL:J6z0LyHP1bsez606_IjAMXrMfqHTbv70I7IJsKuDKA4','2023-05-02 06:37:49.821060'),
('vv7b9isbaoacqldnjnwpbeyyelvsnukp','.eJyrVsrJTFGyMjTXUSrOS8xNVbJS8klVcE7MS8lJLVYISi3OLypRUNJRyslPBqkDKisqSQPr0FEqKQAzagHQGRTQ:1poU5p:2kQK3LnuIU9v7olLluA1vQd7K4HYjFOYhUQNsYRJpcc','2023-05-01 19:00:49.825470');

/*Table structure for table `travel_planning_complaints` */

DROP TABLE IF EXISTS `travel_planning_complaints`;

CREATE TABLE `travel_planning_complaints` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(1000) NOT NULL,
  `date` date NOT NULL,
  `reply` varchar(1000) NOT NULL,
  `userid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `travel_planning_comp_userid_id_ad070cce_fk_travel_pl` (`userid_id`),
  CONSTRAINT `travel_planning_comp_userid_id_ad070cce_fk_travel_pl` FOREIGN KEY (`userid_id`) REFERENCES `travel_planning_userregistration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `travel_planning_complaints` */

insert  into `travel_planning_complaints`(`id`,`complaint`,`date`,`reply`,`userid_id`) values 
(1,'sfdsfds','2023-05-04','ok bye',1),
(2,'jhgfjhgfjh','2023-05-06','jhgfhjfjh',1);

/*Table structure for table `travel_planning_feedback` */

DROP TABLE IF EXISTS `travel_planning_feedback`;

CREATE TABLE `travel_planning_feedback` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `uid_id` bigint NOT NULL,
  `feedbacks` varchar(1000) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `travel_planning_feed_uid_id_ed8871d1_fk_travel_pl` (`uid_id`),
  CONSTRAINT `travel_planning_feed_uid_id_ed8871d1_fk_travel_pl` FOREIGN KEY (`uid_id`) REFERENCES `travel_planning_userregistration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `travel_planning_feedback` */

insert  into `travel_planning_feedback`(`id`,`date`,`uid_id`,`feedbacks`) values 
(1,'2023-05-05',1,'helpful'),
(2,'2023-05-06',1,'');

/*Table structure for table `travel_planning_fooditem` */

DROP TABLE IF EXISTS `travel_planning_fooditem`;

CREATE TABLE `travel_planning_fooditem` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `category` varchar(90) NOT NULL,
  `foodname` varchar(60) NOT NULL,
  `image` varchar(100) NOT NULL,
  `description` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `price` double NOT NULL,
  `restaurantid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `travel_planning_food_restaurantid_id_352faf62_fk_travel_pl` (`restaurantid_id`),
  CONSTRAINT `travel_planning_food_restaurantid_id_352faf62_fk_travel_pl` FOREIGN KEY (`restaurantid_id`) REFERENCES `travel_planning_restaurant` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `travel_planning_fooditem` */

insert  into `travel_planning_fooditem`(`id`,`category`,`foodname`,`image`,`description`,`price`,`restaurantid_id`) values 
(1,'Non-veg','Chicken biriyani','biriyani.jpg','This is A Delectable Dish Prepared out of Rice,chicken, and a melange of spices.this wholesome dish is widely popular in the country and has different regional versions.it is the choice of spices and their balanced use which imparts this dish a unique character.',240,1),
(2,'Burger','Chicken Burger','burger_uJ5DjOE.jpg','healthy food',200,2),
(3,'Non-veg','Ghee Rice','ghee.jpg','Popular And Flavoured South Indian Rice Recipe Made With Basmati Rice And Desi Ghee. It Is One Of The Popular Rice Recipe Made Especially For Celebrations And Occasion Feast Even Though It Is Flavoured. It Needs A Side Dish To Be Served With And More Often It Is Served With Choice Of Kurma Curry Or Gravy Recipe.',150,1),
(4,'Non-veg','Fried Rice','friedrice.jpg','Fried Rice Is A Dish Of Cooked Rice That Has Been Stir-Fried In A Wok Or A Frying Pan And Is Usually Mixed With Other Ingredients Such As Eggs, Vegetables. It Is Often Eaten By Itself Or\'s An Accompaniment To Another Dish',140,1),
(5,'Non-veg','Curd Rice','curd.jpg','Curd Rice le A Sourinaiso Food Made From Procooked Rice Harbe And Tempering Spices.',100,1),
(6,'Non-veg','Mutton Biriyani','mutton.jpg','Mutton Birivanils A Verv Delactable Dish Made Using Mutton And Other Aromatic Substances.',250,1);

/*Table structure for table `travel_planning_login` */

DROP TABLE IF EXISTS `travel_planning_login`;

CREATE TABLE `travel_planning_login` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(90) NOT NULL,
  `password` varchar(90) NOT NULL,
  `type` varchar(90) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `travel_planning_login` */

insert  into `travel_planning_login`(`id`,`username`,`password`,`type`) values 
(1,'pvsanan11@gmail.com','Sanan123','user'),
(7,'paragon@gmail.com','Paragon@123','restaurant'),
(8,'admin','admin','admin'),
(9,'rahmath@gmail.com','Rahmath@123','block'),
(10,'lakkidi@gmail.com','Lakkidi123','block'),
(11,'Midhun@gmail.com','Midhun@123','user'),
(12,'anand@gmail.com','Anand@123','user'),
(14,'mgrill@gmail.com','Mgrill@123','pending'),
(15,'topform@gmail.com','Topform@123','pending'),
(16,'sagar@gmail.com','Sagar@123','restaurant'),
(17,'lecandlesresort@gmail.com','Lecandlesresort123','resort'),
(18,'kadavu@gmail.com','Kadavu123','resort'),
(19,'vayalada@gmail.com','Vayalada123','resort'),
(20,'miracle@gmail.com','Miracle123','resort'),
(21,'taaza@gmail.com','Taaza@123','restaurant'),
(22,'ajwa@gmail.com','Ajwa@123','block');

/*Table structure for table `travel_planning_resortfacility` */

DROP TABLE IF EXISTS `travel_planning_resortfacility`;

CREATE TABLE `travel_planning_resortfacility` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `facility` varchar(60) NOT NULL,
  `description` varchar(70) NOT NULL,
  `image` varchar(100) NOT NULL,
  `resortid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `travel_planning_reso_resortid_id_8cb2980b_fk_travel_pl` (`resortid_id`),
  CONSTRAINT `travel_planning_reso_resortid_id_8cb2980b_fk_travel_pl` FOREIGN KEY (`resortid_id`) REFERENCES `travel_planning_resorts` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `travel_planning_resortfacility` */

insert  into `travel_planning_resortfacility`(`id`,`facility`,`description`,`image`,`resortid_id`) values 
(1,'parking','can park 50plus vehicles','parking_lddvsCV',1),
(2,' parking','Free parking','parking.jpg',2),
(3,' WiFi','Free WiFi','wifi_MuymFP0.jpg',2),
(4,' swimming pool','Outdoor swimming poo','pool.jpg',2);

/*Table structure for table `travel_planning_resortreviewrating` */

DROP TABLE IF EXISTS `travel_planning_resortreviewrating`;

CREATE TABLE `travel_planning_resortreviewrating` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `review` varchar(60) NOT NULL,
  `rating` double NOT NULL,
  `date` date NOT NULL,
  `resortid_id` bigint NOT NULL,
  `uid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `travel_planning_reso_resortid_id_5c3e11e6_fk_travel_pl` (`resortid_id`),
  KEY `travel_planning_reso_uid_id_2213e26a_fk_travel_pl` (`uid_id`),
  CONSTRAINT `travel_planning_reso_resortid_id_5c3e11e6_fk_travel_pl` FOREIGN KEY (`resortid_id`) REFERENCES `travel_planning_resorts` (`id`),
  CONSTRAINT `travel_planning_reso_uid_id_2213e26a_fk_travel_pl` FOREIGN KEY (`uid_id`) REFERENCES `travel_planning_userregistration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `travel_planning_resortreviewrating` */

insert  into `travel_planning_resortreviewrating`(`id`,`review`,`rating`,`date`,`resortid_id`,`uid_id`) values 
(1,'Good',4,'2023-04-11',1,1),
(2,'Amazing Place',3,'2023-04-11',3,2),
(3,'Good Ambiance',3,'2023-04-13',1,2),
(4,'good',3,'2023-04-17',2,1),
(5,'good',2,'2023-04-17',4,2);

/*Table structure for table `travel_planning_resortroom` */

DROP TABLE IF EXISTS `travel_planning_resortroom`;

CREATE TABLE `travel_planning_resortroom` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `roomno` int NOT NULL,
  `type` varchar(20) NOT NULL,
  `image` varchar(100) NOT NULL,
  `amount` double NOT NULL,
  `resortid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `travel_planning_reso_resortid_id_250204b1_fk_travel_pl` (`resortid_id`),
  CONSTRAINT `travel_planning_reso_resortid_id_250204b1_fk_travel_pl` FOREIGN KEY (`resortid_id`) REFERENCES `travel_planning_resorts` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `travel_planning_resortroom` */

insert  into `travel_planning_resortroom`(`id`,`roomno`,`type`,`image`,`amount`,`resortid_id`) values 
(1,101,'AC','lakkidiroom_Ox7oM0h.jpg',1500,1),
(2,101,'AC','le.jpg',4250,2),
(3,102,'AC','lecandlesroom.jpg',3000,2);

/*Table structure for table `travel_planning_resorts` */

DROP TABLE IF EXISTS `travel_planning_resorts`;

CREATE TABLE `travel_planning_resorts` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `phonenumber` bigint NOT NULL,
  `email` varchar(50) NOT NULL,
  `place` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `image` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `district` varchar(50) NOT NULL,
  `license` bigint NOT NULL,
  `lattitude` varchar(1000) NOT NULL,
  `longitude` varchar(1000) NOT NULL,
  `lid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `travel_planning_reso_lid_id_3346500d_fk_travel_pl` (`lid_id`),
  CONSTRAINT `travel_planning_reso_lid_id_3346500d_fk_travel_pl` FOREIGN KEY (`lid_id`) REFERENCES `travel_planning_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `travel_planning_resorts` */

insert  into `travel_planning_resorts`(`id`,`name`,`phonenumber`,`email`,`place`,`image`,`pin`,`district`,`license`,`lattitude`,`longitude`,`lid_id`) values 
(1,'lakkidi resort',956299388,'lakkidi@gmail.com','lakkidi','lakkidi-village-resort_JBkyWBp.jpg',673001,'wayanad,kerala,india',12216017000287,'11.52132355252284','76.02427839526277',10),
(2,'Le Candles Resort ',956299388,'lecandlesresort@gmail.com','East Malayamma Post NIT,calicut','Le Candles Resort .jpg',673001,'kozhikode,kerala,india',12216017000287,'11.32588667746293','75.94428062438965',17),
(3,'The Raviz Kadavu Kozhikode',1234567892,'kadavu@gmail.com','NH17 Calicut Bypass Road,Azhinjilam','kadavuresort.jpg',673001,'Malappuram,kerala,india',12216017000287,'11.496594535537055','75.86651802062988',18),
(4,'Vayalada View Point resort',956299388,'vayalada@gmail.com','NERVEETHI BUSSTOP,vayalada','vayalada.jpg',673001,'kozhikode,kerala,india',12216017000287,'876876','75.86729049682617',19),
(5,'Miracle Resorts',1234567892,'miracle@gmail.com',' Near SteamHouse restaurant, kunnamangalam , Calicut','miracle.jpg',673572,'kozhikode,kerala,india',12216017000287,'11.30617170028184','75.88534981012344',20);

/*Table structure for table `travel_planning_restaurant` */

DROP TABLE IF EXISTS `travel_planning_restaurant`;

CREATE TABLE `travel_planning_restaurant` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `phonenumber` bigint NOT NULL,
  `email` varchar(50) NOT NULL,
  `place` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `image` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `district` varchar(50) NOT NULL,
  `license` bigint NOT NULL,
  `lattitude` varchar(1000) NOT NULL,
  `longitude` varchar(1000) NOT NULL,
  `lid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `travel_planning_rest_lid_id_2b3ab00d_fk_travel_pl` (`lid_id`),
  CONSTRAINT `travel_planning_rest_lid_id_2b3ab00d_fk_travel_pl` FOREIGN KEY (`lid_id`) REFERENCES `travel_planning_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `travel_planning_restaurant` */

insert  into `travel_planning_restaurant`(`id`,`name`,`phonenumber`,`email`,`place`,`image`,`pin`,`district`,`license`,`lattitude`,`longitude`,`lid_id`) values 
(1,'Paragon Restaurant',8281961266,'paragon@gmail.com','kannur Road Near CH Flyover,kozhikode','paragon_EoEau9i.jpg',673572,'kozhikode,Kerala,India',12216017000287,'11.348887673793037','75.93164057050919',7),
(2,'Rahmath Hotel',8597124622,'rahmath@gmail.com','Aravind Ghosa Rd,near mathrubhumi office,kozhikode','rahmath_U8Ghoed.jpg',673572,'Kozhikode,Kerala,India',12216017000287,'11.255310481261871','75.7868242263794',9),
(4,'Mgrill kozhikode',9496777987,'mgrill@gmail.com','Rajaji Road,kozhikode','mgrill.jpg',673001,'Kozhikode,Kerala,India',12216017000287,'11.256370053977637','75.78334759366264',14),
(5,'Topform restaurant',9082468767,'topform@gmail.com','Ground & 1st Floor Golden Plaza Building,Mavoor Rd,Opp Ksrtc,kozhikode','topform.jpg',673001,'Kozhikode,Kerala,India',12216017000287,'11.308642784423187','75.88085833065777',15),
(6,'Hotel sagar kozhikode',82813455787,'sagar@gmail.com','Mavoor Road Nr Mofussil Bus Stand,Arayedathu Palam,Puthiyara,kozhikode','sagar-restaurant.jpg',673001,'Kozhikode,Kerala,India',12216017000287,'11.258898628139596','75.78948497772217',16),
(7,'Taaza Kozhikode',9834125682,'taaza@gmail.com','NH766,wayanad Rd,near IIM Main Gate,kunnamangalam','taaza.jpg',673001,'Kozhikode,Kerala,India',12216017000287,'11.303597601264112','75.87467881136622',21),
(8,'Ajwa Restaurant',7901851266,'ajwa@gmail.com','7XCJ+462,Koolimad,gudalur-nilambur-kozhikode Rd,near diyas auditorium,poolacode','ajwa.jpg',673001,'Kozhikode,Kerala,India',12216017000287,'11.30132902882895','75.85942364515867',22);

/*Table structure for table `travel_planning_restaurantfacility` */

DROP TABLE IF EXISTS `travel_planning_restaurantfacility`;

CREATE TABLE `travel_planning_restaurantfacility` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `facility` varchar(60) NOT NULL,
  `description` varchar(70) NOT NULL,
  `image` varchar(800) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `restaurantid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `travel_planning_rest_restaurantid_id_9c2095c0_fk_travel_pl` (`restaurantid_id`),
  CONSTRAINT `travel_planning_rest_restaurantid_id_9c2095c0_fk_travel_pl` FOREIGN KEY (`restaurantid_id`) REFERENCES `travel_planning_restaurant` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `travel_planning_restaurantfacility` */

insert  into `travel_planning_restaurantfacility`(`id`,`facility`,`description`,`image`,`restaurantid_id`) values 
(1,'car parking','Car parking facility is available which can accomodate 20 cars.','paragon carparking.jpg',1),
(3,'Wifi','free wifi','wifi_PDNocgO.jpg',1);

/*Table structure for table `travel_planning_restaurantreviewrating` */

DROP TABLE IF EXISTS `travel_planning_restaurantreviewrating`;

CREATE TABLE `travel_planning_restaurantreviewrating` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `review` varchar(60) NOT NULL,
  `rating` double NOT NULL,
  `date` date NOT NULL,
  `restaurantid_id` bigint NOT NULL,
  `uid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `travel_planning_rest_restaurantid_id_094b8cdd_fk_travel_pl` (`restaurantid_id`),
  KEY `travel_planning_rest_uid_id_dbdd1c8d_fk_travel_pl` (`uid_id`),
  CONSTRAINT `travel_planning_rest_restaurantid_id_094b8cdd_fk_travel_pl` FOREIGN KEY (`restaurantid_id`) REFERENCES `travel_planning_restaurant` (`id`),
  CONSTRAINT `travel_planning_rest_uid_id_dbdd1c8d_fk_travel_pl` FOREIGN KEY (`uid_id`) REFERENCES `travel_planning_userregistration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `travel_planning_restaurantreviewrating` */

insert  into `travel_planning_restaurantreviewrating`(`id`,`review`,`rating`,`date`,`restaurantid_id`,`uid_id`) values 
(1,'good',4,'2023-04-01',1,1),
(9,'Spicy Food',4,'2023-04-13',1,2),
(10,'Food Waiting Time Is Very Bore',2,'2023-04-13',2,2),
(11,'Good Service',4,'2023-04-13',5,2),
(12,'Tasty Food',4,'2023-04-13',2,3),
(13,'Good Service',4,'2023-04-13',6,3),
(14,'good',2,'2023-04-17',1,3),
(15,'good',2,'2023-04-17',2,3),
(16,'good',3,'2023-04-17',2,3);

/*Table structure for table `travel_planning_touristplace` */

DROP TABLE IF EXISTS `travel_planning_touristplace`;

CREATE TABLE `travel_planning_touristplace` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `place` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  `latitude` varchar(50) NOT NULL,
  `longitude` varchar(50) NOT NULL,
  `description` varchar(10000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `travel_planning_touristplace` */

insert  into `travel_planning_touristplace`(`id`,`place`,`image`,`latitude`,`longitude`,`description`) values 
(1,'Wayanad','wayanad_2Vz1Icz.jpg','11.717219603195328','76.08196450085732','beautiful place'),
(4,'Kozhikode Beach','clct beach_vhnS40Y.jpg','11.263405320335892','75.76495817345732','Kozhikode Beach or Calicut Beach is a beach on the western side of Kozhikode, situated on the Malabar Coast of India. The beach is accessible through four road overbridges in the city. The beach has paved stones and illumination. There is one Lions Park for the children and an aquarium. '),
(5,'Miskhal Masjid','masjid.jpg','11.24974525395982','75.8037200478328','Mishkal Mosque is a medieval mosque located in Calicut on Malabar Coast, southern India. The mosque, one of the few surviving medieval mosques in Kerala, is regarded as an important cultural, historical and architectural monument of Kerala.'),
(6,'Mananchira','mananchira.jpg','11.253881685814434','75.77657135579138','Mananchira is a man-made freshwater pond situated in the centre of the city of Kozhikode (Calicut) in Kerala, southern India. The pond is 3.49 acres (14,120 m2) in area, is rectangular in shape and is fed by a natural spring.'),
(7,'Beypore','beypore.jpg','11.163055592267918','75.80272436141968','Beypore or Beypur is an ancient port town and a locality town in Kozhikode district in the state of Kerala, India. It is located opposite to Chaliyam, the estuary where the river Chaliyar empties into Arabian Sea. Beypore is part of Kozhikode Municipal Corporation');

/*Table structure for table `travel_planning_touristplacereviewrating` */

DROP TABLE IF EXISTS `travel_planning_touristplacereviewrating`;

CREATE TABLE `travel_planning_touristplacereviewrating` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `review` varchar(60) NOT NULL,
  `rating` double NOT NULL,
  `date` date NOT NULL,
  `tpid_id` bigint NOT NULL,
  `uid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `travel_planning_tour_uid_id_28d9373b_fk_travel_pl` (`uid_id`),
  KEY `travel_planning_tour_tpid_id_714dd529_fk_travel_pl` (`tpid_id`),
  CONSTRAINT `travel_planning_tour_tpid_id_714dd529_fk_travel_pl` FOREIGN KEY (`tpid_id`) REFERENCES `travel_planning_touristplace` (`id`),
  CONSTRAINT `travel_planning_tour_uid_id_28d9373b_fk_travel_pl` FOREIGN KEY (`uid_id`) REFERENCES `travel_planning_userregistration` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `travel_planning_touristplacereviewrating` */

insert  into `travel_planning_touristplacereviewrating`(`id`,`review`,`rating`,`date`,`tpid_id`,`uid_id`) values 
(1,'Amazing Place',4,'2023-04-11',1,1),
(2,'Beautiful Place',5,'2023-04-13',1,2),
(4,'Peaceful',4,'2023-04-18',4,1),
(5,'Peaceful',4,'2023-04-18',7,2),
(6,'Peaceful',4,'2023-04-18',6,2);

/*Table structure for table `travel_planning_userregistration` */

DROP TABLE IF EXISTS `travel_planning_userregistration`;

CREATE TABLE `travel_planning_userregistration` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `fullname` varchar(50) NOT NULL,
  `address` varchar(60) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `phonenumber` bigint NOT NULL,
  `email` varchar(50) NOT NULL,
  `lid_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `travel_planning_user_lid_id_7deb9dd0_fk_travel_pl` (`lid_id`),
  CONSTRAINT `travel_planning_user_lid_id_7deb9dd0_fk_travel_pl` FOREIGN KEY (`lid_id`) REFERENCES `travel_planning_login` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `travel_planning_userregistration` */

insert  into `travel_planning_userregistration`(`id`,`fullname`,`address`,`gender`,`phonenumber`,`email`,`lid_id`) values 
(1,'Mohammed sanan','paraparambil','female',7356691060,'pvsanan11@gmail.com',1),
(2,'Midhun','Ak','male',8138813401,'midhun@gmail.com',11),
(3,'Anand','S','male',7907454785,'anand@gmail.com',12);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
