-- MySQL dump 10.13  Distrib 5.7.40, for Win64 (x86_64)
--
-- Host: localhost    Database: oldboy_app01
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
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(40) NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_author`
--

LOCK TABLES `app01_author` WRITE;
/*!40000 ALTER TABLE `app01_author` DISABLE KEYS */;
INSERT INTO `app01_author` VALUES (1,'李','泽雄','zexiong.li@qq.com'),(2,'wu','xinzhe','wuxinzhe@huawei.com'),(3,'haiwei','li','qinhaiwei@huawei.com'),(4,'zhi','duan','duanzhi@huawei.com');
/*!40000 ALTER TABLE `app01_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_book`
--

DROP TABLE IF EXISTS `app01_book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_book` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `publication_date` date NOT NULL,
  `publisher_id` bigint(20) NOT NULL,
  `status` varchar(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `app01_book_publisher_id_e407867a_fk_app01_publisher_id` (`publisher_id`),
  CONSTRAINT `app01_book_publisher_id_e407867a_fk_app01_publisher_id` FOREIGN KEY (`publisher_id`) REFERENCES `app01_publisher` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_book`
--

LOCK TABLES `app01_book` WRITE;
/*!40000 ALTER TABLE `app01_book` DISABLE KEYS */;
INSERT INTO `app01_book` VALUES (1,'人间失格','2023-05-03',1,'producing'),(3,'摆渡人','2023-05-03',1,'published'),(4,'边城','2023-05-03',1,'producing'),(5,'边城','2023-05-03',1,'producing'),(6,'边城','2023-05-03',1,'producing'),(7,'边城','2023-05-03',1,'published'),(8,'modelform','2023-05-10',2,'producing');
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
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_book_authors`
--

LOCK TABLES `app01_book_authors` WRITE;
/*!40000 ALTER TABLE `app01_book_authors` DISABLE KEYS */;
INSERT INTO `app01_book_authors` VALUES (1,1,1),(3,3,1),(4,3,2),(5,8,1),(6,8,2),(7,8,4);
/*!40000 ALTER TABLE `app01_book_authors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app01_publisher`
--

DROP TABLE IF EXISTS `app01_publisher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `app01_publisher` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `address` varchar(50) DEFAULT NULL,
  `city` varchar(60) NOT NULL,
  `state_province` varchar(30) NOT NULL,
  `country` varchar(50) NOT NULL,
  `website` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app01_publisher`
--

LOCK TABLES `app01_publisher` WRITE;
/*!40000 ALTER TABLE `app01_publisher` DISABLE KEYS */;
INSERT INTO `app01_publisher` VALUES (1,'机械工业出版社','沙河地铁站','北京','北京','中国','http://www.jixiegongye.com'),(2,'上海复旦出版社',NULL,'上海','上海','上海','http://www.fudan.com');
/*!40000 ALTER TABLE `app01_publisher` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add author',7,'add_author'),(26,'Can change author',7,'change_author'),(27,'Can delete author',7,'delete_author'),(28,'Can view author',7,'view_author'),(29,'Can add publisher',8,'add_publisher'),(30,'Can change publisher',8,'change_publisher'),(31,'Can delete publisher',8,'delete_publisher'),(32,'Can view publisher',8,'view_publisher'),(33,'Can add book',9,'add_book'),(34,'Can change book',9,'change_book'),(35,'Can delete book',9,'delete_book'),(36,'Can view book',9,'view_book'),(37,'Can add entry',10,'add_entry'),(38,'Can change entry',10,'change_entry'),(39,'Can delete entry',10,'delete_entry'),(40,'Can view entry',10,'view_entry'),(41,'Can add blog',11,'add_blog'),(42,'Can change blog',11,'change_blog'),(43,'Can delete blog',11,'delete_blog'),(44,'Can view blog',11,'view_blog'),(45,'Can add author',12,'add_author'),(46,'Can change author',12,'change_author'),(47,'Can delete author',12,'delete_author'),(48,'Can view author',12,'view_author');
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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$260000$p86EyH4KeDxMnvwVQJ7EaE$Z94X71JIy8EGJZg5UJbkL+zAq+JeqNVUeTxP+zp9NNE=','2023-05-03 12:58:19.623744',1,'lizexiong','','','',1,1,'2023-05-03 12:56:55.872663');
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
-- Table structure for table `blog_author`
--

DROP TABLE IF EXISTS `blog_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_author` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_author`
--

LOCK TABLES `blog_author` WRITE;
/*!40000 ALTER TABLE `blog_author` DISABLE KEYS */;
INSERT INTO `blog_author` VALUES (1,'李泽雄','1043460476@qq.com'),(2,'吴鑫哲','wuxinzhe@huawei.com'),(3,'刘稳','liuwen@huawei.com');
/*!40000 ALTER TABLE `blog_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_blog`
--

DROP TABLE IF EXISTS `blog_blog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_blog` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `tagline` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_blog`
--

LOCK TABLES `blog_blog` WRITE;
/*!40000 ALTER TABLE `blog_blog` DISABLE KEYS */;
INSERT INTO `blog_blog` VALUES (6,'文艺','文艺'),(7,'科技','科技'),(8,'禁书','禁书');
/*!40000 ALTER TABLE `blog_blog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_entry`
--

DROP TABLE IF EXISTS `blog_entry`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_entry` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `headline` varchar(255) NOT NULL,
  `body_text` longtext NOT NULL,
  `pub_date` date NOT NULL,
  `mod_date` date NOT NULL,
  `n_comments` int(11) NOT NULL,
  `n_pingbacks` int(11) NOT NULL,
  `rating` int(11) NOT NULL,
  `blog_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_entry_blog_id_8cd38d8b_fk_blog_blog_id` (`blog_id`),
  CONSTRAINT `blog_entry_blog_id_8cd38d8b_fk_blog_blog_id` FOREIGN KEY (`blog_id`) REFERENCES `blog_blog` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_entry`
--

LOCK TABLES `blog_entry` WRITE;
/*!40000 ALTER TABLE `blog_entry` DISABLE KEYS */;
INSERT INTO `blog_entry` VALUES (1,'边城','边城','2023-05-31','2023-05-31',10000,100,1,6),(2,'人间失格','人间失格','2023-05-10','2023-05-19',100,100,1000,6),(3,'华为创业史','华为创业史','2023-06-01','2023-06-03',1,3,1,7),(4,'金品梅','金品梅','2023-05-24','2023-05-25',10,5,5,7);
/*!40000 ALTER TABLE `blog_entry` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `blog_entry_authors`
--

DROP TABLE IF EXISTS `blog_entry_authors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `blog_entry_authors` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `entry_id` bigint(20) NOT NULL,
  `author_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blog_entry_authors_entry_id_author_id_991f9666_uniq` (`entry_id`,`author_id`),
  KEY `blog_entry_authors_author_id_44edd3c2_fk_blog_author_id` (`author_id`),
  CONSTRAINT `blog_entry_authors_author_id_44edd3c2_fk_blog_author_id` FOREIGN KEY (`author_id`) REFERENCES `blog_author` (`id`),
  CONSTRAINT `blog_entry_authors_entry_id_df89c7c1_fk_blog_entry_id` FOREIGN KEY (`entry_id`) REFERENCES `blog_entry` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `blog_entry_authors`
--

LOCK TABLES `blog_entry_authors` WRITE;
/*!40000 ALTER TABLE `blog_entry_authors` DISABLE KEYS */;
INSERT INTO `blog_entry_authors` VALUES (1,1,1),(2,2,1),(3,3,3),(4,4,2);
/*!40000 ALTER TABLE `blog_entry_authors` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-05-03 13:02:09.240203','1','Author object (1)',1,'[{\"added\": {}}]',7,1),(2,'2023-05-03 13:02:27.135128','2','Author object (2)',1,'[{\"added\": {}}]',7,1),(3,'2023-05-03 13:34:43.029747','1','<机械工业出版社 沙河地铁站>',1,'[{\"added\": {}}]',8,1),(4,'2023-05-03 13:35:09.586017','2','<上海复旦出版社 上海>',1,'[{\"added\": {}}]',8,1),(5,'2023-05-03 13:35:34.124345','1','<人间失格 app01.Author.None <机械工业出版社 沙河地铁站> >',1,'[{\"added\": {}}]',9,1),(6,'2023-05-03 13:35:51.113701','2','<变成 app01.Author.None <上海复旦出版社 上海> >',1,'[{\"added\": {}}]',9,1),(7,'2023-05-03 13:36:18.621099','3','<摆渡人 app01.Author.None <机械工业出版社 沙河地铁站> >',1,'[{\"added\": {}}]',9,1),(8,'2023-05-03 14:05:28.965770','2','<上海复旦出版社 None>',2,'[{\"changed\": {\"fields\": [\"Address\"]}}]',8,1),(9,'2023-05-05 09:00:00.134703','2','<变成 app01.Author.None <上海复旦出版社 None> >',3,'',9,1),(10,'2023-05-06 12:54:32.322997','1','李泽雄',1,'[{\"added\": {}}]',12,1),(11,'2023-05-06 12:54:41.178527','2','吴鑫哲',1,'[{\"added\": {}}]',12,1),(12,'2023-05-06 12:54:54.245173','3','刘稳',1,'[{\"added\": {}}]',12,1),(13,'2023-05-06 12:55:15.910396','1','边城',1,'[{\"added\": {}}]',11,1),(14,'2023-05-06 12:55:22.021175','2','人间失格',1,'[{\"added\": {}}]',11,1),(15,'2023-05-06 12:55:27.453416','3','摆渡人',1,'[{\"added\": {}}]',11,1),(16,'2023-05-06 12:55:41.018330','4','金品梅',1,'[{\"added\": {}}]',11,1),(17,'2023-05-06 12:56:13.717667','5','华为创业史',1,'[{\"added\": {}}]',11,1),(18,'2023-05-06 13:02:49.992047','5','华为创业史',3,'',11,1),(19,'2023-05-06 13:02:49.995535','4','金品梅',3,'',11,1),(20,'2023-05-06 13:02:50.000998','3','摆渡人',3,'',11,1),(21,'2023-05-06 13:02:50.003565','2','人间失格',3,'',11,1),(22,'2023-05-06 13:02:50.006997','1','边城',3,'',11,1),(23,'2023-05-06 13:03:01.251368','6','文艺',1,'[{\"added\": {}}]',11,1),(24,'2023-05-06 13:03:11.261235','7','科技',1,'[{\"added\": {}}]',11,1),(25,'2023-05-06 13:04:26.580970','8','禁书',1,'[{\"added\": {}}]',11,1),(26,'2023-05-06 13:04:58.243659','1','边城',1,'[{\"added\": {}}]',10,1),(27,'2023-05-06 13:05:24.501744','2','人间失格',1,'[{\"added\": {}}]',10,1),(28,'2023-05-06 13:05:50.336730','3','华为创业史',1,'[{\"added\": {}}]',10,1),(29,'2023-05-06 13:06:17.229487','4','金品梅',1,'[{\"added\": {}}]',10,1),(30,'2023-05-06 15:01:42.604545','1','边城',2,'[{\"changed\": {\"fields\": [\"Pub date\", \"Mod date\"]}}]',10,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(7,'app01','author'),(9,'app01','book'),(8,'app01','publisher'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(12,'blog','author'),(11,'blog','blog'),(10,'blog','entry'),(5,'contenttypes','contenttype'),(6,'sessions','session');
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
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-05-03 12:50:03.248423'),(2,'auth','0001_initial','2023-05-03 12:50:04.332924'),(3,'admin','0001_initial','2023-05-03 12:50:04.671423'),(4,'admin','0002_logentry_remove_auto_add','2023-05-03 12:50:04.709924'),(5,'admin','0003_logentry_add_action_flag_choices','2023-05-03 12:50:04.747425'),(6,'app01','0001_initial','2023-05-03 12:50:05.310424'),(7,'contenttypes','0002_remove_content_type_name','2023-05-03 12:50:05.498922'),(8,'auth','0002_alter_permission_name_max_length','2023-05-03 12:50:05.606423'),(9,'auth','0003_alter_user_email_max_length','2023-05-03 12:50:05.721923'),(10,'auth','0004_alter_user_username_opts','2023-05-03 12:50:05.762929'),(11,'auth','0005_alter_user_last_login_null','2023-05-03 12:50:05.880931'),(12,'auth','0006_require_contenttypes_0002','2023-05-03 12:50:05.898926'),(13,'auth','0007_alter_validators_add_error_messages','2023-05-03 12:50:05.938924'),(14,'auth','0008_alter_user_username_max_length','2023-05-03 12:50:06.071923'),(15,'auth','0009_alter_user_last_name_max_length','2023-05-03 12:50:06.229425'),(16,'auth','0010_alter_group_name_max_length','2023-05-03 12:50:06.369428'),(17,'auth','0011_update_proxy_permissions','2023-05-03 12:50:06.414926'),(18,'auth','0012_alter_user_first_name_max_length','2023-05-03 12:50:06.545425'),(19,'sessions','0001_initial','2023-05-03 12:50:06.651426'),(20,'app01','0002_alter_publisher_address','2023-05-03 14:02:51.351740'),(21,'app01','0003_auto_20230505_2335','2023-05-05 15:35:13.878744'),(22,'blog','0001_initial','2023-05-06 04:36:02.551225');
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
INSERT INTO `django_session` VALUES ('z58tyaix3y7y1ec0djvxmjev0vi597m8','.eJxVjDsOwjAQRO_iGln-fyjpOYO1Xm9wADlSnFSIu4OlFFCNNO_NvFiCfatp77SmubAzk-z022XAB7UByh3abeG4tG2dMx8KP2jn16XQ83K4fwcVev2uLYAjp0P2MYoSlTERnA_TJG2wugQQirQGLMJ6UkZLSUEhIY4QINj7A9BAN6E:1puC3n:VqykA3tRYl9o0rdoQpWTpDmqpliFz-XUn_YMBFc7beE','2023-05-17 12:58:19.628245');
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

-- Dump completed on 2023-05-07 18:14:13
