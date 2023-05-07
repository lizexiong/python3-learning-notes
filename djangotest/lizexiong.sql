-- MySQL dump 10.13  Distrib 5.7.40, for Win64 (x86_64)
--
-- Host: localhost    Database: lizexiong
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
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add test',7,'add_test'),(26,'Can change test',7,'change_test'),(27,'Can delete test',7,'delete_test'),(28,'Can view test',7,'view_test'),(29,'Can add tag',8,'add_tag'),(30,'Can change tag',8,'change_tag'),(31,'Can delete tag',8,'delete_tag'),(32,'Can view tag',8,'view_tag'),(33,'Can add contact',9,'add_contact'),(34,'Can change contact',9,'change_contact'),(35,'Can delete contact',9,'delete_contact'),(36,'Can view contact',9,'view_contact');
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
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$260000$jAa9le1f8Mgl3Njh9MUsE0$SI6c3O3pV7BYAzFW7c+lIQt9UukWLyRy9XGwBIJi1kg=','2023-04-30 18:24:01.251457',1,'admin','','','',1,1,'2023-04-30 18:23:23.864573');
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
-- Table structure for table `classesandteachersrelationship`
--

DROP TABLE IF EXISTS `classesandteachersrelationship`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classesandteachersrelationship` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `fk_teacher_id` int(11) NOT NULL COMMENT '教师记录',
  `fk_class_id` int(11) NOT NULL COMMENT '班级记录',
  PRIMARY KEY (`id`),
  UNIQUE KEY `fk_teacher_id` (`fk_teacher_id`,`fk_class_id`),
  KEY `fk_class_id` (`fk_class_id`),
  CONSTRAINT `classesandteachersrelationship_ibfk_1` FOREIGN KEY (`fk_teacher_id`) REFERENCES `teachersinfo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `classesandteachersrelationship_ibfk_2` FOREIGN KEY (`fk_class_id`) REFERENCES `classesinfo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classesandteachersrelationship`
--

LOCK TABLES `classesandteachersrelationship` WRITE;
/*!40000 ALTER TABLE `classesandteachersrelationship` DISABLE KEYS */;
INSERT INTO `classesandteachersrelationship` VALUES (1,1,1),(2,1,2),(3,1,3),(4,2,1),(5,3,3);
/*!40000 ALTER TABLE `classesandteachersrelationship` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `classesinfo`
--

DROP TABLE IF EXISTS `classesinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `classesinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `number` int(11) NOT NULL COMMENT '班级编号',
  `name` varchar(64) NOT NULL COMMENT '班级名称',
  `fk_teacher_id` int(11) NOT NULL COMMENT '班级负责人',
  PRIMARY KEY (`id`),
  UNIQUE KEY `number` (`number`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `fk_teacher_id` (`fk_teacher_id`),
  CONSTRAINT `classesinfo_ibfk_1` FOREIGN KEY (`fk_teacher_id`) REFERENCES `teachersinfo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `classesinfo`
--

LOCK TABLES `classesinfo` WRITE;
/*!40000 ALTER TABLE `classesinfo` DISABLE KEYS */;
INSERT INTO `classesinfo` VALUES (1,1601,'one year one class',1),(2,1602,'one year two class',2),(3,1603,'one year three class',3);
/*!40000 ALTER TABLE `classesinfo` ENABLE KEYS */;
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
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2023-04-30 18:39:29.178857','1','Contact object (1)',1,'[{\"added\": {}}]',9,1),(2,'2023-04-30 18:39:58.340744','1','Contact object (1)',2,'[{\"added\": {\"name\": \"tag\", \"object\": \"Tag object (1)\"}}, {\"added\": {\"name\": \"tag\", \"object\": \"Tag object (2)\"}}, {\"added\": {\"name\": \"tag\", \"object\": \"Tag object (3)\"}}]',9,1),(3,'2023-04-30 18:40:16.744766','1','Contact object (1)',3,'',9,1),(4,'2023-04-30 18:40:46.667661','2','Contact object (2)',1,'[{\"added\": {}}]',9,1),(5,'2023-04-30 18:41:50.196325','3','Contact object (3)',1,'[{\"added\": {}}]',9,1);
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
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(9,'TestModel','contact'),(8,'TestModel','tag'),(7,'TestModel','test');
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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2023-04-30 14:18:48.484171'),(2,'auth','0001_initial','2023-04-30 14:18:48.834186'),(3,'admin','0001_initial','2023-04-30 14:18:48.915186'),(4,'admin','0002_logentry_remove_auto_add','2023-04-30 14:18:48.925187'),(5,'admin','0003_logentry_add_action_flag_choices','2023-04-30 14:18:48.933186'),(6,'contenttypes','0002_remove_content_type_name','2023-04-30 14:18:48.994186'),(7,'auth','0002_alter_permission_name_max_length','2023-04-30 14:18:49.027186'),(8,'auth','0003_alter_user_email_max_length','2023-04-30 14:18:49.064188'),(9,'auth','0004_alter_user_username_opts','2023-04-30 14:18:49.071186'),(10,'auth','0005_alter_user_last_login_null','2023-04-30 14:18:49.102186'),(11,'auth','0006_require_contenttypes_0002','2023-04-30 14:18:49.105186'),(12,'auth','0007_alter_validators_add_error_messages','2023-04-30 14:18:49.113187'),(13,'auth','0008_alter_user_username_max_length','2023-04-30 14:18:49.149102'),(14,'auth','0009_alter_user_last_name_max_length','2023-04-30 14:18:49.186102'),(15,'auth','0010_alter_group_name_max_length','2023-04-30 14:18:49.223104'),(16,'auth','0011_update_proxy_permissions','2023-04-30 14:18:49.231102'),(17,'auth','0012_alter_user_first_name_max_length','2023-04-30 14:18:49.266102'),(18,'sessions','0001_initial','2023-04-30 14:18:49.292102'),(19,'TestModel','0001_initial','2023-04-30 14:20:23.947714'),(20,'TestModel','0002_contact_tag','2023-04-30 18:32:55.577913');
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
INSERT INTO `django_session` VALUES ('51ue7a175w10s5gr5k8eoeflekst4v6z','.eJxVjMsOwiAQRf-FtSHA0BFcuu83NDMw2KqBpI-V8d-1SRe6veec-1IDbes4bIvMw5TVRVl1-t2Y0kPqDvKd6q3p1Oo6T6x3RR900X3L8rwe7t_BSMv4rY3DDjJGm8hwSZ0J4JJHAQ5cECVSEF88eS5iHcaz7QJycMWBARNBvT_ZlzdE:1ptBi4:QBLdixSZ243btMVmaNQlJ5H4i3OWulwoIfk8PzORoiI','2023-05-14 18:23:44.979009'),('9kpxc1hl8sef75m43k4iea0ch517033c','.eJxVjMsOwiAQRf-FtSHA0BFcuu83NDMw2KqBpI-V8d-1SRe6veec-1IDbes4bIvMw5TVRVl1-t2Y0kPqDvKd6q3p1Oo6T6x3RR900X3L8rwe7t_BSMv4rY3DDjJGm8hwSZ0J4JJHAQ5cECVSEF88eS5iHcaz7QJycMWBARNBvT_ZlzdE:1ptBiL:jKjwF0uMByWJmb5Qf-QVb_NNYrNrSF-RLMxbFzFRqLo','2023-05-14 18:24:01.253465');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studentsinfo`
--

DROP TABLE IF EXISTS `studentsinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `studentsinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(64) NOT NULL COMMENT '学生姓名',
  `gender` enum('male','female') NOT NULL COMMENT '学生性别',
  `age` int(11) NOT NULL COMMENT '学生年龄',
  `fk_student_id` int(11) NOT NULL COMMENT '学生编号',
  `fk_class_id` int(11) DEFAULT NULL COMMENT '班级编号',
  PRIMARY KEY (`id`),
  KEY `fk_student_id` (`fk_student_id`),
  KEY `fk_class_id` (`fk_class_id`),
  CONSTRAINT `studentsinfo_ibfk_1` FOREIGN KEY (`fk_student_id`) REFERENCES `studentsnumberinfo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `studentsinfo_ibfk_2` FOREIGN KEY (`fk_class_id`) REFERENCES `classesinfo` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studentsinfo`
--

LOCK TABLES `studentsinfo` WRITE;
/*!40000 ALTER TABLE `studentsinfo` DISABLE KEYS */;
INSERT INTO `studentsinfo` VALUES (1,'Jack','male',17,1,2),(2,'Tom','male',18,2,1),(3,'Mary','female',16,3,3),(4,'Anna','female',17,4,1),(5,'Bobby','male',18,6,2);
/*!40000 ALTER TABLE `studentsinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `studentsnumberinfo`
--

DROP TABLE IF EXISTS `studentsnumberinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `studentsnumberinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `number` int(11) NOT NULL COMMENT '学生编号',
  `admission` date NOT NULL COMMENT '入学时间',
  `graduation` date NOT NULL COMMENT '毕业时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `number` (`number`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `studentsnumberinfo`
--

LOCK TABLES `studentsnumberinfo` WRITE;
/*!40000 ALTER TABLE `studentsnumberinfo` DISABLE KEYS */;
INSERT INTO `studentsnumberinfo` VALUES (1,160201,'2016-09-01','2021-06-15'),(2,160101,'2016-09-01','2021-06-15'),(3,160301,'2016-09-01','2021-06-15'),(4,160102,'2016-09-01','2021-06-15'),(5,160302,'2016-09-01','2021-06-15'),(6,160202,'2016-09-01','2021-06-15');
/*!40000 ALTER TABLE `studentsnumberinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachersinfo`
--

DROP TABLE IF EXISTS `teachersinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `teachersinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `number` int(11) NOT NULL COMMENT '教师编号',
  `name` varchar(64) NOT NULL COMMENT '教师姓名',
  `gender` enum('male','female') NOT NULL COMMENT '教师性别',
  `age` int(11) NOT NULL COMMENT '教师年龄',
  PRIMARY KEY (`id`),
  UNIQUE KEY `number` (`number`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachersinfo`
--

LOCK TABLES `teachersinfo` WRITE;
/*!40000 ALTER TABLE `teachersinfo` DISABLE KEYS */;
INSERT INTO `teachersinfo` VALUES (1,3341,'David','male',32),(2,3342,'Jason','male',30),(3,3343,'Lisa','female',28);
/*!40000 ALTER TABLE `teachersinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testmodel_contact`
--

DROP TABLE IF EXISTS `testmodel_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testmodel_contact` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `age` int(11) NOT NULL,
  `email` varchar(254) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testmodel_contact`
--

LOCK TABLES `testmodel_contact` WRITE;
/*!40000 ALTER TABLE `testmodel_contact` DISABLE KEYS */;
INSERT INTO `testmodel_contact` VALUES (2,'alibaba',20,'1043460476@qq.com'),(3,'google',3,'1043460476@qq.com');
/*!40000 ALTER TABLE `testmodel_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testmodel_tag`
--

DROP TABLE IF EXISTS `testmodel_tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testmodel_tag` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `contact_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `TestModel_tag_contact_id_05dff71d_fk_TestModel_contact_id` (`contact_id`),
  CONSTRAINT `TestModel_tag_contact_id_05dff71d_fk_TestModel_contact_id` FOREIGN KEY (`contact_id`) REFERENCES `testmodel_contact` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testmodel_tag`
--

LOCK TABLES `testmodel_tag` WRITE;
/*!40000 ALTER TABLE `testmodel_tag` DISABLE KEYS */;
/*!40000 ALTER TABLE `testmodel_tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `testmodel_test`
--

DROP TABLE IF EXISTS `testmodel_test`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `testmodel_test` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `testmodel_test`
--

LOCK TABLES `testmodel_test` WRITE;
/*!40000 ALTER TABLE `testmodel_test` DISABLE KEYS */;
/*!40000 ALTER TABLE `testmodel_test` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo`
--

DROP TABLE IF EXISTS `userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(32) NOT NULL COMMENT '姓名',
  `age` int(11) NOT NULL COMMENT '年龄',
  `phone` decimal(6,0) NOT NULL COMMENT '手机号',
  `address` varchar(64) NOT NULL COMMENT '地址',
  `gender` enum('male','female') DEFAULT NULL COMMENT '性别',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `last_update_time` datetime DEFAULT NULL COMMENT '最后更新时间',
  `delete_status` tinyint(1) DEFAULT NULL COMMENT '是否删除',
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone` (`phone`),
  KEY `ix_userInfo_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo`
--

LOCK TABLES `userinfo` WRITE;
/*!40000 ALTER TABLE `userinfo` DISABLE KEYS */;
INSERT INTO `userinfo` VALUES (1,'Jackson',19,330621,'Beijing','male','2023-03-24 11:51:17','2023-03-24 12:26:34',0),(3,'Tom',19,330624,'Shanghai','male','2023-03-24 12:22:33',NULL,0);
/*!40000 ALTER TABLE `userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo2`
--

DROP TABLE IF EXISTS `userinfo2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfo2` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(32) NOT NULL COMMENT '姓名',
  `age` int(11) NOT NULL COMMENT '年龄',
  `phone` decimal(6,0) NOT NULL COMMENT '手机号',
  `address` varchar(64) NOT NULL COMMENT '地址',
  `gender` enum('male','female') DEFAULT NULL COMMENT '性别',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `last_update_time` datetime DEFAULT NULL COMMENT '最后更新时间',
  `delete_status` tinyint(1) DEFAULT NULL COMMENT '是否删除',
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone` (`phone`),
  KEY `ix_userInfo2_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo2`
--

LOCK TABLES `userinfo2` WRITE;
/*!40000 ALTER TABLE `userinfo2` DISABLE KEYS */;
/*!40000 ALTER TABLE `userinfo2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo3`
--

DROP TABLE IF EXISTS `userinfo3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfo3` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键',
  `name` varchar(32) NOT NULL COMMENT '姓名',
  `age` int(11) NOT NULL COMMENT '年龄',
  `phone` decimal(6,0) NOT NULL COMMENT '手机号',
  `address` varchar(64) NOT NULL COMMENT '地址',
  `gender` enum('male','female') DEFAULT NULL COMMENT '性别',
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `last_update_time` datetime DEFAULT NULL COMMENT '最后更新时间',
  `delete_status` tinyint(1) DEFAULT NULL COMMENT '是否删除',
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone` (`phone`),
  KEY `ix_userInfo3_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo3`
--

LOCK TABLES `userinfo3` WRITE;
/*!40000 ALTER TABLE `userinfo3` DISABLE KEYS */;
/*!40000 ALTER TABLE `userinfo3` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-07 18:17:29
