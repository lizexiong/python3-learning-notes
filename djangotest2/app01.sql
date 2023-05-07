-- MySQL dump 10.13  Distrib 5.7.40, for Win64 (x86_64)
--
-- Host: localhost    Database: app01
-- ------------------------------------------------------
-- Server version	5.7.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `app01_author`
--

DROP TABLE IF EXISTS `app01_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_author` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `age` smallint(6) NOT NULL,
  `au_detail_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `au_detail_id` (`au_detail_id`),
  CONSTRAINT `app01_author_au_detail_id_440c948c_fk_app01_authordetail_id` FOREIGN KEY (`au_detail_id`) REFERENCES `app01_authordetail` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_author`
--

LOCK TABLES `app01_author` WRITE;
/*!40000 ALTER TABLE `app01_author` DISABLE KEYS */;
INSERT INTO `app01_author` VALUES (1,'令狐冲',25,1),(2,'任我行',58,2),(3,'任盈盈',23,3);
/*!40000 ALTER TABLE `app01_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_authordetail`
--

DROP TABLE IF EXISTS `app01_authordetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_authordetail` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `gender` smallint(6) NOT NULL,
  `tel` varchar(32) NOT NULL,
  `addr` varchar(64) NOT NULL,
  `birthday` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_authordetail`
--

LOCK TABLES `app01_authordetail` WRITE;
/*!40000 ALTER TABLE `app01_authordetail` DISABLE KEYS */;
INSERT INTO `app01_authordetail` VALUES (1,1,'13432335433','华山','1994-05-23'),(2,1,'13943454554','黑木崖','1961-08-13'),(3,0,'13878934322','黑木崖','1996-05-20');
/*!40000 ALTER TABLE `app01_authordetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_book`
--

DROP TABLE IF EXISTS `app01_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_book` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  `price` decimal(5,2) NOT NULL,
  `publish_id` bigint(20) NOT NULL,
  `pub_date` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app01_book_publish_id_d96d3535` (`publish_id`),
  CONSTRAINT `app01_book_publish_id_d96d3535_fk_app01_publish_id` FOREIGN KEY (`publish_id`) REFERENCES `app01_publish` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_book`
--

LOCK TABLES `app01_book` WRITE;
/*!40000 ALTER TABLE `app01_book` DISABLE KEYS */;
INSERT INTO `app01_book` VALUES (1,'李泽雄',300.00,1,'2010-10-10'),(2,'冲灵剑法',200.00,1,'2004-04-04'),(3,'吸星大法',400.00,2,'1999-09-19');
/*!40000 ALTER TABLE `app01_book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_book_authors`
--

DROP TABLE IF EXISTS `app01_book_authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_book_authors` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `book_id` bigint(20) NOT NULL,
  `author_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app01_book_authors_book_id_author_id_36f1e11a_uniq` (`book_id`,`author_id`),
  KEY `app01_book_authors_author_id_5acae95a_fk_app01_author_id` (`author_id`),
  CONSTRAINT `app01_book_authors_author_id_5acae95a_fk_app01_author_id` FOREIGN KEY (`author_id`) REFERENCES `app01_author` (`id`),
  CONSTRAINT `app01_book_authors_book_id_19c7077f_fk_app01_book_id` FOREIGN KEY (`book_id`) REFERENCES `app01_book` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_book_authors`
--

LOCK TABLES `app01_book_authors` WRITE;
/*!40000 ALTER TABLE `app01_book_authors` DISABLE KEYS */;
INSERT INTO `app01_book_authors` VALUES (1,1,1),(2,1,3),(3,2,1),(7,2,3),(10,3,2);
/*!40000 ALTER TABLE `app01_book_authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_dep`
--

DROP TABLE IF EXISTS `app01_dep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_dep` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_dep`
--

LOCK TABLES `app01_dep` WRITE;
/*!40000 ALTER TABLE `app01_dep` DISABLE KEYS */;
INSERT INTO `app01_dep` VALUES (1,'销售部'),(2,'关公部');
/*!40000 ALTER TABLE `app01_dep` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_emp`
--

DROP TABLE IF EXISTS `app01_emp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_emp` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `age` int(11) NOT NULL,
  `salary` decimal(8,2) NOT NULL,
  `dep` varchar(32) NOT NULL,
  `province` varchar(32) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_emp`
--

LOCK TABLES `app01_emp` WRITE;
/*!40000 ALTER TABLE `app01_emp` DISABLE KEYS */;
INSERT INTO `app01_emp` VALUES (1,'令狐冲',24,6000.00,'销售部','河南'),(2,'任盈盈',18,8000.00,'关公部','广东'),(3,'任我行',56,10000.00,'销售部','广东'),(4,'岳灵珊',19,6000.00,'关公部','河南'),(5,'小龙女',20,8000.00,'关公部','河北');
/*!40000 ALTER TABLE `app01_emp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_emps`
--

DROP TABLE IF EXISTS `app01_emps`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_emps` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `age` int(11) NOT NULL,
  `salary` decimal(8,2) NOT NULL,
  `province` varchar(32) NOT NULL,
  `dep_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app01_emps_dep_id_4b309329_fk_app01_dep_id` (`dep_id`),
  CONSTRAINT `app01_emps_dep_id_4b309329_fk_app01_dep_id` FOREIGN KEY (`dep_id`) REFERENCES `app01_dep` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_emps`
--

LOCK TABLES `app01_emps` WRITE;
/*!40000 ALTER TABLE `app01_emps` DISABLE KEYS */;
INSERT INTO `app01_emps` VALUES (2,'令狐冲',24,8000.00,'河南',1),(3,'任盈盈',18,9000.00,'广东',2),(4,'任我行',57,10000.00,'广东',1),(5,'岳灵珊',19,6000.00,'河南',2),(6,'小龙女',20,8000.00,'河北',2);
/*!40000 ALTER TABLE `app01_emps` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_publish`
--

DROP TABLE IF EXISTS `app01_publish`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_publish` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) NOT NULL,
  `city` varchar(64) NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_publish`
--

LOCK TABLES `app01_publish` WRITE;
/*!40000 ALTER TABLE `app01_publish` DISABLE KEYS */;
INSERT INTO `app01_publish` VALUES (1,'华山出版社','华山','hs@163.com'),(2,'明教出版社','黑木崖','mj@163.com');
/*!40000 ALTER TABLE `app01_publish` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_userinfo`
--

DROP TABLE IF EXISTS `app01_userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_userinfo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_userinfo`
--

LOCK TABLES `app01_userinfo` WRITE;
/*!40000 ALTER TABLE `app01_userinfo` DISABLE KEYS */;
INSERT INTO `app01_userinfo` VALUES (1,'lizexiong','123');
/*!40000 ALTER TABLE `app01_userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add book',7,'add_book'),(26,'Can change book',7,'change_book'),(27,'Can delete book',7,'delete_book'),(28,'Can view book',7,'view_book'),(29,'Can add author detail',8,'add_authordetail'),(30,'Can change author detail',8,'change_authordetail'),(31,'Can delete author detail',8,'delete_authordetail'),(32,'Can view author detail',8,'view_authordetail'),(33,'Can add publish',9,'add_publish'),(34,'Can change publish',9,'change_publish'),(35,'Can delete publish',9,'delete_publish'),(36,'Can view publish',9,'view_publish'),(37,'Can add author',10,'add_author'),(38,'Can change author',10,'change_author'),(39,'Can delete author',10,'delete_author'),(40,'Can view author',10,'view_author'),(41,'Can add emp',11,'add_emp'),(42,'Can change emp',11,'change_emp'),(43,'Can delete emp',11,'delete_emp'),(44,'Can view emp',11,'view_emp'),(45,'Can add dep',12,'add_dep'),(46,'Can change dep',12,'change_dep'),(47,'Can delete dep',12,'delete_dep'),(48,'Can view dep',12,'view_dep'),(49,'Can add emps',13,'add_emps'),(50,'Can change emps',13,'change_emps'),(51,'Can delete emps',13,'delete_emps'),(52,'Can view emps',13,'view_emps'),(53,'Can add user info',14,'add_userinfo'),(54,'Can change user info',14,'change_userinfo'),(55,'Can delete user info',14,'delete_userinfo'),(56,'Can view user info',14,'view_userinfo'),(57,'Can add user info',15,'add_userinfo'),(58,'Can change user info',15,'change_userinfo'),(59,'Can delete user info',15,'delete_userinfo'),(60,'Can view user info',15,'view_userinfo');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
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
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (14,'123',NULL,0,'lizexiong','','','',0,1,'2023-05-01 10:23:50.603586');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cookie_userinfo`
--

DROP TABLE IF EXISTS `cookie_userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cookie_userinfo` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(64) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cookie_userinfo`
--

LOCK TABLES `cookie_userinfo` WRITE;
/*!40000 ALTER TABLE `cookie_userinfo` DISABLE KEYS */;
INSERT INTO `cookie_userinfo` VALUES (1,'lizexiong','123');
/*!40000 ALTER TABLE `cookie_userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(10,'app01','author'),(8,'app01','authordetail'),(7,'app01','book'),(12,'app01','dep'),(11,'app01','emp'),(13,'app01','emps'),(9,'app01','publish'),(14,'app01','userinfo'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(15,'cookie','userinfo'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-05-01 08:11:09.300340'),(2,'auth','0001_initial','2023-05-01 08:11:09.840259'),(3,'admin','0001_initial','2023-05-01 08:11:09.984256'),(4,'admin','0002_logentry_remove_auto_add','2023-05-01 08:11:10.003258'),(5,'admin','0003_logentry_add_action_flag_choices','2023-05-01 08:11:10.017257'),(6,'app01','0001_initial','2023-05-01 08:11:10.054260'),(7,'app01','0002_auto_20230501_1605','2023-05-01 08:11:10.504271'),(8,'contenttypes','0002_remove_content_type_name','2023-05-01 08:11:10.603350'),(9,'auth','0002_alter_permission_name_max_length','2023-05-01 08:11:10.660350'),(10,'auth','0003_alter_user_email_max_length','2023-05-01 08:11:10.721355'),(11,'auth','0004_alter_user_username_opts','2023-05-01 08:11:10.739357'),(12,'auth','0005_alter_user_last_login_null','2023-05-01 08:11:10.788356'),(13,'auth','0006_require_contenttypes_0002','2023-05-01 08:11:10.797353'),(14,'auth','0007_alter_validators_add_error_messages','2023-05-01 08:11:10.813356'),(15,'auth','0008_alter_user_username_max_length','2023-05-01 08:11:10.866355'),(16,'auth','0009_alter_user_last_name_max_length','2023-05-01 08:11:10.931353'),(17,'auth','0010_alter_group_name_max_length','2023-05-01 08:11:11.001374'),(18,'auth','0011_update_proxy_permissions','2023-05-01 08:11:11.020374'),(19,'auth','0012_alter_user_first_name_max_length','2023-05-01 08:11:11.075458'),(20,'sessions','0001_initial','2023-05-01 08:11:11.121439'),(21,'app01','0003_dep_emp_emps','2023-05-01 08:55:19.854079'),(22,'app01','0004_userinfo','2023-05-01 10:22:52.529630'),(23,'cookie','0001_initial','2023-05-01 10:36:48.569967');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-07 18:17:20
