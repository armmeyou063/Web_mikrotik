-- MySQL dump 10.13  Distrib 8.0.29, for Win64 (x86_64)
--
-- Host: localhost    Database: mikrotik
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=125 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add bridge',7,'add_bridge'),(26,'Can change bridge',7,'change_bridge'),(27,'Can delete bridge',7,'delete_bridge'),(28,'Can view bridge',7,'view_bridge'),(29,'Can add port',8,'add_port'),(30,'Can change port',8,'change_port'),(31,'Can delete port',8,'delete_port'),(32,'Can view port',8,'view_port'),(33,'Can add ethernet',9,'add_ethernet'),(34,'Can change ethernet',9,'change_ethernet'),(35,'Can delete ethernet',9,'delete_ethernet'),(36,'Can view ethernet',9,'view_ethernet'),(37,'Can add interface',10,'add_interface'),(38,'Can change interface',10,'change_interface'),(39,'Can delete interface',10,'delete_interface'),(40,'Can view interface',10,'view_interface'),(41,'Can add vlan',11,'add_vlan'),(42,'Can change vlan',11,'change_vlan'),(43,'Can delete vlan',11,'delete_vlan'),(44,'Can view vlan',11,'view_vlan'),(45,'Can add vlans',12,'add_vlans'),(46,'Can change vlans',12,'change_vlans'),(47,'Can delete vlans',12,'delete_vlans'),(48,'Can view vlans',12,'view_vlans'),(49,'Can add dhcpclient',13,'add_dhcpclient'),(50,'Can change dhcpclient',13,'change_dhcpclient'),(51,'Can delete dhcpclient',13,'delete_dhcpclient'),(52,'Can view dhcpclient',13,'view_dhcpclient'),(53,'Can add dhcpnetwork',14,'add_dhcpnetwork'),(54,'Can change dhcpnetwork',14,'change_dhcpnetwork'),(55,'Can delete dhcpnetwork',14,'delete_dhcpnetwork'),(56,'Can view dhcpnetwork',14,'view_dhcpnetwork'),(57,'Can add dhcpserver',15,'add_dhcpserver'),(58,'Can change dhcpserver',15,'change_dhcpserver'),(59,'Can delete dhcpserver',15,'delete_dhcpserver'),(60,'Can view dhcpserver',15,'view_dhcpserver'),(61,'Can add ipaddress',16,'add_ipaddress'),(62,'Can change ipaddress',16,'change_ipaddress'),(63,'Can delete ipaddress',16,'delete_ipaddress'),(64,'Can view ipaddress',16,'view_ipaddress'),(65,'Can add dhcpclienttype',17,'add_dhcpclienttype'),(66,'Can change dhcpclienttype',17,'change_dhcpclienttype'),(67,'Can delete dhcpclienttype',17,'delete_dhcpclienttype'),(68,'Can view dhcpclienttype',17,'view_dhcpclienttype'),(69,'Can add pool',18,'add_pool'),(70,'Can change pool',18,'change_pool'),(71,'Can delete pool',18,'delete_pool'),(72,'Can view pool',18,'view_pool'),(73,'Can add dhcplease',19,'add_dhcplease'),(74,'Can change dhcplease',19,'change_dhcplease'),(75,'Can delete dhcplease',19,'delete_dhcplease'),(76,'Can view dhcplease',19,'view_dhcplease'),(77,'Can add route',20,'add_route'),(78,'Can change route',20,'change_route'),(79,'Can delete route',20,'delete_route'),(80,'Can view route',20,'view_route'),(81,'Can add identity',21,'add_identity'),(82,'Can change identity',21,'change_identity'),(83,'Can delete identity',21,'delete_identity'),(84,'Can view identity',21,'view_identity'),(85,'Can add user',22,'add_user'),(86,'Can change user',22,'change_user'),(87,'Can delete user',22,'delete_user'),(88,'Can view user',22,'view_user'),(89,'Can add dns',23,'add_dns'),(90,'Can change dns',23,'change_dns'),(91,'Can delete dns',23,'delete_dns'),(92,'Can view dns',23,'view_dns'),(93,'Can add connection',24,'add_connection'),(94,'Can change connection',24,'change_connection'),(95,'Can delete connection',24,'delete_connection'),(96,'Can view connection',24,'view_connection'),(97,'Can add server',25,'add_server'),(98,'Can change server',25,'change_server'),(99,'Can delete server',25,'delete_server'),(100,'Can view server',25,'view_server'),(101,'Can add serverprofile',26,'add_serverprofile'),(102,'Can change serverprofile',26,'change_serverprofile'),(103,'Can delete serverprofile',26,'delete_serverprofile'),(104,'Can view serverprofile',26,'view_serverprofile'),(105,'Can add hotspotuser',27,'add_hotspotuser'),(106,'Can change hotspotuser',27,'change_hotspotuser'),(107,'Can delete hotspotuser',27,'delete_hotspotuser'),(108,'Can view hotspotuser',27,'view_hotspotuser'),(109,'Can add userprofile',28,'add_userprofile'),(110,'Can change userprofile',28,'change_userprofile'),(111,'Can delete userprofile',28,'delete_userprofile'),(112,'Can view userprofile',28,'view_userprofile'),(113,'Can add binding',29,'add_binding'),(114,'Can change binding',29,'change_binding'),(115,'Can delete binding',29,'delete_binding'),(116,'Can view binding',29,'view_binding'),(117,'Can add host',30,'add_host'),(118,'Can change host',30,'change_host'),(119,'Can delete host',30,'delete_host'),(120,'Can view host',30,'view_host'),(121,'Can add users',27,'add_users'),(122,'Can change users',27,'change_users'),(123,'Can delete users',27,'delete_users'),(124,'Can view users',27,'view_users');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `first_name` varchar(30) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `last_name` varchar(150) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `email` varchar(254) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext CHARACTER SET utf8 COLLATE utf8_bin,
  `object_repr` varchar(200) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
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
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `model` varchar(100) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(29,'network','binding'),(7,'network','bridge'),(24,'network','connection'),(13,'network','dhcpclient'),(17,'network','dhcpclienttype'),(19,'network','dhcplease'),(14,'network','dhcpnetwork'),(15,'network','dhcpserver'),(23,'network','dns'),(9,'network','ethernet'),(30,'network','host'),(21,'network','identity'),(10,'network','interface'),(16,'network','ipaddress'),(18,'network','pool'),(8,'network','port'),(20,'network','route'),(25,'network','server'),(26,'network','serverprofile'),(22,'network','user'),(28,'network','userprofile'),(27,'network','users'),(11,'network','vlan'),(12,'network','vlans'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `name` varchar(255) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'network','0001_initial','2022-04-23 06:29:02.994921'),(2,'network','0002_port','2022-04-23 11:38:47.044213'),(3,'network','0003_ethernet_interface_vlan','2022-04-24 13:39:45.058388'),(4,'network','0004_auto_20220424_2135','2022-04-24 14:36:00.589156'),(5,'network','0005_auto_20220424_2139','2022-04-24 14:39:24.712484'),(6,'network','0006_vlans','2022-04-24 17:32:31.142128'),(7,'contenttypes','0001_initial','2022-04-26 07:14:09.629175'),(8,'auth','0001_initial','2022-04-26 07:14:09.850179'),(9,'admin','0001_initial','2022-04-26 07:14:10.454174'),(10,'admin','0002_logentry_remove_auto_add','2022-04-26 07:14:10.571174'),(11,'admin','0003_logentry_add_action_flag_choices','2022-04-26 07:14:10.580175'),(12,'contenttypes','0002_remove_content_type_name','2022-04-26 07:14:10.687175'),(13,'auth','0002_alter_permission_name_max_length','2022-04-26 07:14:10.751173'),(14,'auth','0003_alter_user_email_max_length','2022-04-26 07:14:10.826173'),(15,'auth','0004_alter_user_username_opts','2022-04-26 07:14:10.837176'),(16,'auth','0005_alter_user_last_login_null','2022-04-26 07:14:11.003176'),(17,'auth','0006_require_contenttypes_0002','2022-04-26 07:14:11.010174'),(18,'auth','0007_alter_validators_add_error_messages','2022-04-26 07:14:11.021175'),(19,'auth','0008_alter_user_username_max_length','2022-04-26 07:14:11.107208'),(20,'auth','0009_alter_user_last_name_max_length','2022-04-26 07:14:11.181173'),(21,'auth','0010_alter_group_name_max_length','2022-04-26 07:14:11.246174'),(22,'auth','0011_update_proxy_permissions','2022-04-26 07:14:11.257174'),(23,'sessions','0001_initial','2022-04-26 07:14:11.317173'),(24,'network','0007_vlans_tagged1','2022-04-26 08:53:07.235159'),(25,'network','0008_remove_vlans_tagged1','2022-04-26 11:50:44.765865'),(26,'network','0009_dhcpclient_dhcpnetwork_dhcpserver_ipaddress','2022-04-26 15:15:50.776579'),(27,'network','0010_auto_20220426_2313','2022-04-26 16:13:15.359811'),(28,'network','0011_dhcpclienttype','2022-04-26 16:45:30.432828'),(29,'network','0012_pool','2022-04-27 04:04:13.728089'),(30,'network','0013_dhcpnetwork_dns','2022-04-27 06:40:18.320739'),(31,'network','0014_dhcplease','2022-04-27 07:25:10.725888'),(32,'network','0015_route','2022-04-27 08:08:02.558732'),(33,'network','0016_auto_20220427_1949','2022-04-27 12:49:54.461472'),(34,'network','0017_identity_user','2022-04-27 15:24:28.546551'),(35,'network','0018_dns','2022-04-27 16:55:48.285331'),(36,'network','0019_connection','2022-04-27 17:37:01.070884'),(37,'network','0020_auto_20220429_2157','2022-04-29 14:57:20.985051'),(38,'network','0021_auto_20220429_2212','2022-04-29 15:12:34.109325'),(39,'network','0022_auto_20220429_2248','2022-04-29 15:50:33.731358'),(40,'network','0023_auto_20220429_2249','2022-04-29 15:50:34.043963'),(41,'network','0024_auto_20220429_2250','2022-04-29 15:50:34.157816'),(42,'network','0025_hotspotuser_userprofile','2022-04-29 15:51:09.657961'),(43,'network','0026_binding_host','2022-04-29 15:52:22.855163'),(44,'network','0027_auto_20220429_2252','2022-04-29 15:52:22.929707'),(45,'network','0028_serverprofile_ser_id','2022-04-29 16:38:00.286975'),(46,'network','0029_remove_serverprofile_ser_profile','2022-04-29 16:41:13.503588'),(47,'network','0030_serverprofile_ser_dns','2022-04-30 13:06:23.902715'),(48,'network','0031_auto_20220501_2241','2022-05-01 15:41:56.928252'),(49,'network','0032_binding_binding_address','2022-05-01 16:41:30.751154'),(50,'network','0033_route_dynamic','2022-05-02 13:51:27.013670');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `session_data` longtext CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_binding`
--

DROP TABLE IF EXISTS `network_binding`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_binding` (
  `id` int NOT NULL AUTO_INCREMENT,
  `binding_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `binding_mac` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `binding_ser` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `binding_type` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `binding_address` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_binding`
--

LOCK TABLES `network_binding` WRITE;
/*!40000 ALTER TABLE `network_binding` DISABLE KEYS */;
/*!40000 ALTER TABLE `network_binding` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_bridge`
--

DROP TABLE IF EXISTS `network_bridge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_bridge` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `typebridge` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `actualmtu` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `l2mtu` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `vlan` tinyint(1) NOT NULL,
  `bridge_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=762 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_bridge`
--

LOCK TABLES `network_bridge` WRITE;
/*!40000 ALTER TABLE `network_bridge` DISABLE KEYS */;
INSERT INTO `network_bridge` VALUES (757,'LAN','Bridge','1500','1598',0,'*83'),(758,'MAN12','Bridge','1500','65535',0,'*7C'),(759,'WAN','Bridge','1500','65535',0,'*6E'),(760,'arm159439','Bridge','1500','65535',0,'*7B'),(761,'tot123','Bridge','1500','65535',1,'*7F');
/*!40000 ALTER TABLE `network_bridge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_connection`
--

DROP TABLE IF EXISTS `network_connection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_connection` (
  `id` int NOT NULL AUTO_INCREMENT,
  `con_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `protocal` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `src` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `dst` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `reply_src` varchar(60) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `reply_dst` varchar(60) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `repl_byte` varchar(60) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `repl_packet` varchar(60) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `orig_packet` varchar(60) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `orig_byte` varchar(60) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1271 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_connection`
--

LOCK TABLES `network_connection` WRITE;
/*!40000 ALTER TABLE `network_connection` DISABLE KEYS */;
INSERT INTO `network_connection` VALUES (1069,'*433','tcp','192.168.10.247:49845','17.57.145.149:5223','17.57.145.149:5223','192.168.1.100:49845','4975','13','18','8236'),(1070,'*434','tcp','192.168.10.246:62057','17.57.145.150:5223','17.57.145.150:5223','192.168.1.100:62057','5606','18','22','9449'),(1071,'*435','tcp','192.168.10.246:51649','52.98.65.2:443','52.98.65.2:443','192.168.1.100:51649','4904','8','11','2993'),(1072,'*436','tcp','192.168.10.246:52513','40.99.8.194:443','40.99.8.194:443','192.168.1.100:52513','4904','8','11','2981'),(1073,'*437','tcp','192.168.10.246:52477','52.98.90.2:443','52.98.90.2:443','192.168.1.100:52477','6460','10','13','3255'),(1074,'*438','tcp','192.168.10.247:49780','17.57.145.138:5223','17.57.145.138:5223','192.168.1.100:49780','4924','12','18','8236'),(1075,'*439','tcp','192.168.10.247:49723','17.57.145.150:5223','17.57.145.150:5223','192.168.1.100:49723','4976','13','19','8288'),(1076,'*43A','tcp','192.168.10.250:54440','52.45.56.185:80','52.45.56.185:80','192.168.1.100:54440','264','3','4','449'),(1077,'*43B','tcp','192.168.10.246:54643','17.57.145.132:5223','17.57.145.132:5223','192.168.1.100:54643','5206','17','25','11115'),(1078,'*43C','tcp','192.168.10.247:50825','17.57.145.137:5223','17.57.145.137:5223','192.168.1.100:50825','4974','13','22','8457'),(1079,'*43D','tcp','192.168.10.246:61425','40.100.29.242:443','40.100.29.242:443','192.168.1.100:61425','6396','9','13','3109'),(1080,'*43E','tcp','192.168.10.247:49737','17.57.145.54:5223','17.57.145.54:5223','192.168.1.100:49737','4975','13','18','8236'),(1081,'*43F','tcp','192.168.10.246:52525','52.98.84.114:443','52.98.84.114:443','192.168.1.100:52525','4906','8','11','2981'),(1082,'*440','tcp','192.168.10.247:49859','17.57.145.55:5223','17.57.145.55:5223','192.168.1.100:49859','4923','12','19','8288'),(1083,'*441','tcp','192.168.10.246:52520','49.231.116.211:443','49.231.116.211:443','192.168.1.100:52520','133991','96','64','4198'),(1084,'*442','tcp','192.168.10.246:52427','49.231.116.208:443','49.231.116.208:443','192.168.1.100:52427','133898','95','66','4302'),(1085,'*443','tcp','192.168.10.246:63606','40.99.10.2:443','40.99.10.2:443','192.168.1.100:63606','6461','10','13','3267'),(1086,'*444','tcp','192.168.10.247:49732','17.57.145.55:5223','17.57.145.55:5223','192.168.1.100:49732','4924','12','18','8235'),(1087,'*445','tcp','192.168.10.247:57387','34.102.215.99:443','34.102.215.99:443','192.168.1.100:57387','15911','97','73','15281'),(1088,'*446','tcp','192.168.10.246:52558','40.99.10.98:443','40.99.10.98:443','192.168.1.100:52558','4852','7','9','2700'),(1089,'*447','tcp','192.168.10.246:54627','40.99.10.18:443','40.99.10.18:443','192.168.1.100:54627','4908','8','11','2981'),(1090,'*448','tcp','192.168.10.246:63626','17.57.145.148:5223','17.57.145.148:5223','192.168.1.100:63626','5599','16','24','9585'),(1091,'*449','tcp','192.168.10.246:54610','17.57.145.150:5223','17.57.145.150:5223','192.168.1.100:54610','4976','13','20','9275'),(1092,'*44A','tcp','192.168.10.245:55563','117.18.237.29:80','117.18.237.29:80','192.168.1.100:55563','2079','6','4','408'),(1093,'*44B','tcp','192.168.10.247:58901','34.102.215.99:443','34.102.215.99:443','192.168.1.100:58901','20826','133','107','17358'),(1094,'*44C','tcp','192.168.10.246:54654','52.98.90.178:443','52.98.90.178:443','192.168.1.100:54654','4854','7','11','2981'),(1095,'*44D','tcp','192.168.10.246:54618','17.57.145.54:5223','17.57.145.54:5223','192.168.1.100:54618','4975','13','21','9325'),(1096,'*44E','tcp','192.168.10.247:49812','17.57.145.136:5223','17.57.145.136:5223','192.168.1.100:49812','4976','13','19','8288'),(1097,'*44F','tcp','192.168.10.247:50810','17.57.145.134:5223','17.57.145.134:5223','192.168.1.100:50810','4975','13','16','8132'),(1098,'*450','tcp','192.168.10.247:65110','74.125.68.109:993','74.125.68.109:993','192.168.1.100:65110','8182','33','33','3169'),(1099,'*451','tcp','192.168.10.246:51708','17.57.145.138:5223','17.57.145.138:5223','192.168.1.100:51708','6067','21','27','9785'),(1100,'*452','tcp','192.168.10.247:57323','49.231.114.211:443','49.231.114.211:443','192.168.1.100:57323','8068','25','26','15382'),(1101,'*453','tcp','192.168.10.246:51638','52.98.37.2:443','52.98.37.2:443','192.168.1.100:51638','4904','8','11','2993'),(1102,'*454','tcp','192.168.10.247:49851','17.57.145.133:5223','17.57.145.133:5223','192.168.1.100:49851','4922','12','18','8236'),(1103,'*455','tcp','192.168.10.246:63409','40.99.10.82:443','40.99.10.82:443','192.168.1.100:63409','4904','8','11','2981'),(1104,'*456','tcp','192.168.10.247:57375','23.32.72.17:443','23.32.72.17:443','192.168.1.100:57375','21241','39','38','21697'),(1105,'*457','tcp','192.168.10.247:57394','49.231.112.32:443','49.231.112.32:443','192.168.1.100:57394','11074','35','30','21523'),(1106,'*458','tcp','192.168.10.246:52622','52.98.54.130:443','52.98.54.130:443','192.168.1.100:52622','4969','9','12','3562'),(1107,'*459','tcp','192.168.10.246:52528','52.98.84.82:443','52.98.84.82:443','192.168.1.100:52528','4908','8','12','3033'),(1108,'*45A','tcp','192.168.10.246:63636','49.231.116.211:443','49.231.116.211:443','192.168.1.100:63636','6957','9','11','1437'),(1109,'*45B','tcp','192.168.10.247:51051','17.57.145.149:5223','17.57.145.149:5223','192.168.1.100:51051','5232','17','23','8538'),(1110,'*45C','tcp','192.168.10.245:55715','96.16.126.47:443','96.16.126.47:443','192.168.1.100:55715','7763','12','10','1051'),(1111,'*45D','tcp','192.168.10.246:52535','52.98.70.130:443','52.98.70.130:443','192.168.1.100:52535','4904','8','12','3033'),(1112,'*45E','tcp','192.168.10.247:50831','17.57.145.133:5223','17.57.145.133:5223','192.168.1.100:50831','4923','12','17','8183'),(1113,'*45F','tcp','192.168.10.246:52614','52.98.90.178:443','52.98.90.178:443','192.168.1.100:52614','4906','8','11','2981'),(1114,'*460','tcp','192.168.10.246:63470','17.57.145.148:5223','17.57.145.148:5223','192.168.1.100:63470','7548','32','36','10434'),(1115,'*461','tcp','192.168.10.246:52672','40.99.10.114:443','40.99.10.114:443','192.168.1.100:52672','4916','8','10','2910'),(1116,'*462','tcp','192.168.10.247:50783','17.145.16.2:443','17.145.16.2:443','192.168.1.100:50783','57298','59','50','6213'),(1117,'*463','tcp','192.168.10.246:52411','104.18.32.68:80','104.18.32.68:80','192.168.1.100:52411','525','4','5','578'),(1118,'*465','tcp','192.168.10.245:55578','40.99.10.50:443','40.99.10.50:443','192.168.1.100:55578','6837','9','10','2497'),(1119,'*466','tcp','192.168.10.246:61410','52.98.65.18:443','52.98.65.18:443','192.168.1.100:61410','4852','7','11','2981'),(1120,'*467','tcp','192.168.10.245:55649','40.90.189.152:443','40.90.189.152:443','192.168.1.100:55649','26777','113','212','14520'),(1121,'*468','tcp','192.168.10.247:50784','17.57.145.149:5223','17.57.145.149:5223','192.168.1.100:50784','5233','17','24','8590'),(1122,'*469','tcp','192.168.10.247:49764','17.57.145.148:5223','17.57.145.148:5223','192.168.1.100:49764','4975','13','18','8236'),(1123,'*46A','tcp','192.168.10.246:54571','52.98.54.130:443','52.98.54.130:443','192.168.1.100:54571','4853','7','11','2993'),(1124,'*46B','tcp','192.168.10.246:54535','52.98.33.162:443','52.98.33.162:443','192.168.1.100:54535','5022','10','13','3243'),(1125,'*46C','tcp','192.168.10.247:50799','17.57.145.137:5223','17.57.145.137:5223','192.168.1.100:50799','4975','13','24','8572'),(1126,'*46D','tcp','192.168.10.246:51627','40.99.10.98:443','40.99.10.98:443','192.168.1.100:51627','4852','7','12','3045'),(1127,'*46E','tcp','192.168.10.247:49769','17.57.145.138:5223','17.57.145.138:5223','192.168.1.100:49769','4976','13','18','8236'),(1128,'*46F','tcp','192.168.10.246:61397','40.99.10.2:443','40.99.10.2:443','192.168.1.100:61397','4905','8','11','2981'),(1129,'*470','tcp','192.168.10.246:54578','17.57.145.137:5223','17.57.145.137:5223','192.168.1.100:54578','5913','18','27','9686'),(1130,'*471','tcp','192.168.10.247:59075','49.231.116.90:443','49.231.116.90:443','192.168.1.100:59075','18163','20','18','7546'),(1131,'*472','tcp','192.168.10.246:63619','52.98.37.2:443','52.98.37.2:443','192.168.1.100:63619','4852','7','11','2993'),(1132,'*473','tcp','192.168.10.246:52693','40.99.10.18:443','40.99.10.18:443','192.168.1.100:52693','4908','8','11','2981'),(1133,'*474','tcp','192.168.10.246:54548','23.194.59.30:443','23.194.59.30:443','192.168.1.100:54548','9395','14','13','1608'),(1134,'*475','tcp','192.168.10.246:52430','40.99.10.50:443','40.99.10.50:443','192.168.1.100:52430','4908','8','12','3033'),(1135,'*476','tcp','192.168.10.246:54650','23.194.59.30:443','23.194.59.30:443','192.168.1.100:54650','9395','14','16','1764'),(1136,'*477','tcp','192.168.10.246:61181','17.57.145.135:5223','17.57.145.135:5223','192.168.1.100:61181','6122','26','36','10274'),(1137,'*478','tcp','192.168.10.247:50566','17.57.145.150:5223','17.57.145.150:5223','192.168.1.100:50566','4976','13','19','8287'),(1138,'*479','tcp','192.168.10.246:52597','17.57.145.136:5223','17.57.145.136:5223','192.168.1.100:52597','4975','13','20','9274'),(1139,'*47A','tcp','192.168.10.247:50573','17.57.145.132:5223','17.57.145.132:5223','192.168.1.100:50573','4975','13','19','8288'),(1140,'*47B','tcp','192.168.10.247:50843','17.57.145.149:5223','17.57.145.149:5223','192.168.1.100:50843','4976','13','20','8340'),(1141,'*47C','tcp','192.168.10.247:49871','17.57.145.150:5223','17.57.145.150:5223','192.168.1.100:49871','4975','13','18','8235'),(1142,'*47D','tcp','192.168.10.247:65116','17.57.145.150:5223','17.57.145.150:5223','192.168.1.100:65116','4922','12','20','8340'),(1143,'*47E','tcp','192.168.10.246:52702','17.57.145.137:5223','17.57.145.137:5223','192.168.1.100:52702','8231','35','40','10582'),(1144,'*47F','tcp','192.168.10.246:52619','40.99.10.34:443','40.99.10.34:443','192.168.1.100:52619','4856','7','11','2981'),(1145,'*480','tcp','192.168.10.246:52290','40.99.8.194:443','40.99.8.194:443','192.168.1.100:52290','6396','9','12','3045'),(1146,'*481','tcp','192.168.10.246:52641','40.99.10.34:443','40.99.10.34:443','192.168.1.100:52641','4856','7','11','2981'),(1147,'*482','tcp','192.168.10.246:54507','17.57.145.133:5223','17.57.145.133:5223','192.168.1.100:54507','5115','15','22','10842'),(1148,'*483','tcp','192.168.10.246:54556','40.99.10.34:443','40.99.10.34:443','192.168.1.100:54556','4972','9','12','3175'),(1149,'*484','tcp','192.168.10.246:51661','17.57.145.135:5223','17.57.145.135:5223','192.168.1.100:51661','4975','13','21','9326'),(1150,'*485','tcp','192.168.10.246:52598','17.57.145.136:5223','17.57.145.136:5223','192.168.1.100:52598','7047','28','34','10177'),(1151,'*486','tcp','192.168.10.246:54573','17.57.145.148:5223','17.57.145.148:5223','192.168.1.100:54573','4975','13','20','9283'),(1152,'*487','tcp','192.168.10.247:50816','17.57.145.135:5223','17.57.145.135:5223','192.168.1.100:50816','4975','13','17','8184'),(1153,'*488','tcp','192.168.10.246:54598','40.99.10.98:443','40.99.10.98:443','192.168.1.100:54598','4852','7','11','2981'),(1154,'*489','tcp','192.168.10.246:63070','52.98.84.98:443','52.98.84.98:443','192.168.1.100:63070','4904','8','11','2981'),(1155,'*48A','tcp','192.168.10.246:63540','52.98.54.130:443','52.98.54.130:443','192.168.1.100:63540','4905','8','10','2929'),(1156,'*48B','tcp','192.168.10.247:49949','17.57.145.134:5223','17.57.145.134:5223','192.168.1.100:49949','8461','27','31','9056'),(1157,'*48C','tcp','192.168.10.246:52499','40.99.10.82:443','40.99.10.82:443','192.168.1.100:52499','4852','7','10','2929'),(1158,'*48D','tcp','192.168.10.246:52526','49.231.116.211:443','49.231.116.211:443','192.168.1.100:52526','7010','10','10','1373'),(1159,'*48E','tcp','192.168.10.246:51693','40.99.10.98:443','40.99.10.98:443','192.168.1.100:51693','4916','8','12','4473'),(1160,'*48F','tcp','192.168.10.246:61401','52.98.33.130:443','52.98.33.130:443','192.168.1.100:61401','4906','8','10','2929'),(1161,'*490','tcp','192.168.10.246:52518','40.99.10.34:443','40.99.10.34:443','192.168.1.100:52518','4856','7','12','3033'),(1162,'*491','tcp','192.168.10.246:51620','40.99.10.82:443','40.99.10.82:443','192.168.1.100:51620','4852','7','12','3045'),(1163,'*492','tcp','192.168.10.247:65253','74.125.200.109:993','74.125.200.109:993','192.168.1.100:65253','8511','35','35','3269'),(1164,'*493','tcp','192.168.10.246:63580','52.98.40.34:443','52.98.40.34:443','192.168.1.100:63580','4905','8','10','2941'),(1165,'*494','tcp','192.168.10.246:51685','52.98.84.98:443','52.98.84.98:443','192.168.1.100:51685','4904','8','11','2981'),(1166,'*495','tcp','192.168.10.246:62062','17.57.145.138:5223','17.57.145.138:5223','192.168.1.100:62062','4974','13','18','9170'),(1167,'*496','tcp','192.168.10.247:49855','17.57.145.136:5223','17.57.145.136:5223','192.168.1.100:49855','8322','21','27','8788'),(1168,'*497','tcp','192.168.10.247:49751','17.57.145.55:5223','17.57.145.55:5223','192.168.1.100:49751','4975','13','18','8235'),(1169,'*498','tcp','192.168.10.246:52434','49.231.116.208:443','49.231.116.208:443','192.168.1.100:52434','7010','10','12','1477'),(1170,'*499','tcp','192.168.10.246:52474','17.57.145.54:5223','17.57.145.54:5223','192.168.1.100:52474','4974','13','18','9171'),(1171,'*49A','tcp','192.168.10.247:59076','49.231.114.240:443','49.231.114.240:443','192.168.1.100:59076','4281','14','14','8059'),(1172,'*49B','tcp','192.168.10.246:51690','17.57.145.150:5223','17.57.145.150:5223','192.168.1.100:51690','4976','13','21','9325'),(1173,'*49C','tcp','192.168.10.246:51628','17.57.145.132:5223','17.57.145.132:5223','192.168.1.100:51628','6277','20','27','9722'),(1174,'*49D','tcp','192.168.10.246:52582','52.98.54.130:443','52.98.54.130:443','192.168.1.100:52582','4905','8','11','2981'),(1175,'*49E','tcp','192.168.10.247:57321','34.102.215.99:443','34.102.215.99:443','192.168.1.100:57321','14915','93','66','12625'),(1176,'*49F','tcp','192.168.10.246:51660','23.220.184.25:443','23.220.184.25:443','192.168.1.100:51660','9395','14','13','1608'),(1177,'*4A0','tcp','192.168.10.246:54534','17.57.145.148:5223','17.57.145.148:5223','192.168.1.100:54534','4924','12','20','9273'),(1178,'*4A2','tcp','192.168.10.247:51366','17.57.145.148:5223','17.57.145.148:5223','192.168.1.100:51366','4975','13','18','8235'),(1179,'*4A3','tcp','192.168.10.246:62079','52.98.65.2:443','52.98.65.2:443','192.168.1.100:62079','4904','8','11','2981'),(1180,'*4A5','tcp','192.168.10.246:63631','17.57.145.136:5223','17.57.145.136:5223','192.168.1.100:63631','6026','19','25','9661'),(1181,'*4A6','tcp','192.168.10.246:54514','17.57.145.132:5223','17.57.145.132:5223','192.168.1.100:54514','5027','14','20','9274'),(1182,'*4A7','tcp','192.168.10.246:61406','40.99.10.98:443','40.99.10.98:443','192.168.1.100:61406','4852','7','11','2981'),(1183,'*4A8','tcp','192.168.10.246:54579','52.98.84.114:443','52.98.84.114:443','192.168.1.100:54579','4970','9','12','4485'),(1184,'*4A9','tcp','192.168.10.246:51710','40.99.10.2:443','40.99.10.2:443','192.168.1.100:51710','4905','8','11','2981'),(1185,'*4AA','tcp','192.168.10.246:52443','52.98.70.130:443','52.98.70.130:443','192.168.1.100:52443','4904','8','11','2981'),(1186,'*4AB','tcp','192.168.10.246:51647','17.57.145.150:5223','17.57.145.150:5223','192.168.1.100:51647','6130','21','27','9722'),(1187,'*4AC','tcp','192.168.10.246:52420','52.98.54.130:443','52.98.54.130:443','192.168.1.100:52420','4905','8','11','2981'),(1188,'*4AD','tcp','192.168.10.246:52574','40.100.29.242:443','40.100.29.242:443','192.168.1.100:52574','4852','7','12','3033'),(1189,'*4AE','tcp','192.168.10.250:54460','40.119.211.203:443','40.119.211.203:443','192.168.1.100:54460','5053','12','12','2529'),(1190,'*4AF','tcp','192.168.10.246:63635','49.231.116.211:443','49.231.116.211:443','192.168.1.100:63635','132995','93','65','4262'),(1191,'*4B0','tcp','192.168.10.247:49795','17.57.145.134:5223','17.57.145.134:5223','192.168.1.100:49795','4974','13','20','8339'),(1192,'*4B1','udp','192.168.10.254:48967','192.168.10.254:5246','192.168.10.254:5246','192.168.1.100:48967','850290','7495','7493','1063500'),(1193,'*4B2','tcp','192.168.10.247:49822','17.57.145.135:5223','17.57.145.135:5223','192.168.1.100:49822','4975','13','18','8236'),(1194,'*4B3','tcp','192.168.10.246:54634','52.98.71.50:443','52.98.71.50:443','192.168.1.100:54634','4904','8','11','2981'),(1195,'*4B4','tcp','192.168.10.246:51675','40.99.10.34:443','40.99.10.34:443','192.168.1.100:51675','4856','7','11','2981'),(1196,'*4B5','tcp','192.168.10.245:55716','117.18.237.29:80','117.18.237.29:80','192.168.1.100:55716','2079','6','4','414'),(1197,'*4B6','tcp','192.168.10.246:54521','52.98.50.66:443','52.98.50.66:443','192.168.1.100:54521','4853','7','12','3045'),(1198,'*4B7','tcp','192.168.10.246:52678','52.98.54.130:443','52.98.54.130:443','192.168.1.100:52678','4853','7','10','2752'),(1199,'*4B8','tcp','192.168.10.246:51632','40.99.10.50:443','40.99.10.50:443','192.168.1.100:51632','4908','8','11','2993'),(1200,'*4B9','tcp','192.168.10.246:51694','17.57.145.138:5223','17.57.145.138:5223','192.168.1.100:51694','4922','12','20','9274'),(1201,'*4BA','tcp','192.168.10.246:52532','40.99.10.2:443','40.99.10.2:443','192.168.1.100:52532','4905','8','11','2981'),(1202,'*4BB','tcp','192.168.10.246:52661','52.98.65.178:443','52.98.65.178:443','192.168.1.100:52661','4904','8','11','2981'),(1203,'*4BC','tcp','192.168.10.246:54652','17.57.145.134:5223','17.57.145.134:5223','192.168.1.100:54652','4975','13','18','9169'),(1204,'*4BD','tcp','192.168.10.246:54519','17.57.145.55:5223','17.57.145.55:5223','192.168.1.100:54519','4974','13','21','9327'),(1205,'*4BE','tcp','192.168.10.246:52527','17.57.145.132:5223','17.57.145.132:5223','192.168.1.100:52527','5658','19','24','9551'),(1206,'*4BF','tcp','192.168.10.246:52489','40.99.8.194:443','40.99.8.194:443','192.168.1.100:52489','4852','7','11','2981'),(1207,'*4C0','tcp','192.168.10.247:57376','23.32.72.17:443','23.32.72.17:443','192.168.1.100:57376','17167','24','15','7457'),(1208,'*4C1','tcp','192.168.10.246:52425','40.99.10.50:443','40.99.10.50:443','192.168.1.100:52425','4856','7','12','3033'),(1209,'*4C2','tcp','192.168.10.246:52534','17.57.145.136:5223','17.57.145.136:5223','192.168.1.100:52534','4975','13','19','9221'),(1210,'*4C3','tcp','192.168.10.247:50758','17.57.145.133:5223','17.57.145.133:5223','192.168.1.100:50758','5104','15','22','8471'),(1211,'*4C4','tcp','192.168.10.246:63605','17.57.145.148:5223','17.57.145.148:5223','192.168.1.100:63605','6916','26','33','10181'),(1212,'*4C5','tcp','192.168.10.246:52628','52.98.54.130:443','52.98.54.130:443','192.168.1.100:52628','4905','8','11','2981'),(1213,'*4C6','tcp','192.168.10.246:52465','40.99.10.82:443','40.99.10.82:443','192.168.1.100:52465','5096','11','14','5252'),(1214,'*4C7','tcp','192.168.10.246:52480','52.98.65.18:443','52.98.65.18:443','192.168.1.100:52480','4904','8','10','2929'),(1215,'*4C8','tcp','192.168.10.247:49806','17.57.145.149:5223','17.57.145.149:5223','192.168.1.100:49806','4922','12','18','8236'),(1216,'*4C9','tcp','192.168.10.246:63595','40.99.10.98:443','40.99.10.98:443','192.168.1.100:63595','4968','9','12','3203'),(1217,'*4CA','tcp','192.168.10.246:51643','40.99.10.82:443','40.99.10.82:443','192.168.1.100:51643','4852','7','11','2993'),(1218,'*4CB','tcp','192.168.10.246:63632','52.98.33.130:443','52.98.33.130:443','192.168.1.100:63632','4906','8','11','2993'),(1219,'*4CC','tcp','192.168.10.246:60954','52.98.65.2:443','52.98.65.2:443','192.168.1.100:60954','4904','8','11','2993'),(1220,'*4CD','tcp','192.168.10.247:65257','17.57.145.150:5223','17.57.145.150:5223','192.168.1.100:65257','4923','12','17','8183'),(1221,'*4CE','tcp','192.168.10.246:61180','40.99.10.82:443','40.99.10.82:443','192.168.1.100:61180','4852','7','11','2993'),(1222,'*4CF','tcp','192.168.10.246:52604','52.98.33.162:443','52.98.33.162:443','192.168.1.100:52604','4906','8','11','2981'),(1223,'*4D0','tcp','192.168.10.246:51695','52.98.90.2:443','52.98.90.2:443','192.168.1.100:51695','4852','7','11','2981'),(1224,'*4D1','tcp','192.168.10.247:50575','17.57.145.149:5223','17.57.145.149:5223','192.168.1.100:50575','5647','24','39','18248'),(1225,'*4D2','tcp','192.168.10.246:54518','49.231.116.211:443','49.231.116.211:443','192.168.1.100:54518','7009','10','12','1477'),(1226,'*4D3','tcp','192.168.10.246:52576','52.98.65.178:443','52.98.65.178:443','192.168.1.100:52576','4852','7','11','2981'),(1227,'*4D4','tcp','192.168.10.246:61413','49.231.120.171:443','49.231.120.171:443','192.168.1.100:61413','7010','10','13','1529'),(1228,'*4D5','tcp','192.168.10.250:54461','40.119.211.203:443','40.119.211.203:443','192.168.1.100:54461','5329','13','12','3084'),(1229,'*4D6','tcp','192.168.10.247:49711','17.57.145.135:5223','17.57.145.135:5223','192.168.1.100:49711','4975','13','20','8339'),(1230,'*4D7','tcp','192.168.10.246:52431','17.57.145.136:5223','17.57.145.136:5223','192.168.1.100:52431','6599','25','34','10154'),(1231,'*4D8','tcp','192.168.10.247:50830','49.231.116.208:443','49.231.116.208:443','192.168.1.100:50830','7011','10','13','1531'),(1232,'*4D9','tcp','192.168.10.246:54616','17.57.145.149:5223','17.57.145.149:5223','192.168.1.100:54616','4974','13','20','9283'),(1233,'*4DA','tcp','192.168.10.246:63627','40.99.10.2:443','40.99.10.2:443','192.168.1.100:63627','4853','7','11','2993'),(1234,'*4DB','tcp','192.168.10.246:62084','40.99.10.50:443','40.99.10.50:443','192.168.1.100:62084','4908','8','11','2981'),(1235,'*4DC','tcp','192.168.10.246:51655','40.99.10.66:443','40.99.10.66:443','192.168.1.100:51655','4904','8','11','2993'),(1236,'*4DD','tcp','192.168.10.246:63585','40.99.10.34:443','40.99.10.34:443','192.168.1.100:63585','4856','7','10','2941'),(1237,'*4DE','tcp','192.168.10.246:54584','17.57.145.148:5223','17.57.145.148:5223','192.168.1.100:54584','4976','13','21','9326'),(1238,'*4DF','tcp','192.168.10.246:51654','17.57.145.134:5223','17.57.145.134:5223','192.168.1.100:51654','6132','21','28','9773'),(1239,'*4E0','tcp','192.168.10.246:52701','40.99.10.114:443','40.99.10.114:443','192.168.1.100:52701','4904','8','11','2981'),(1240,'*4E1','tcp','192.168.10.246:54611','52.98.54.130:443','52.98.54.130:443','192.168.1.100:54611','4969','9','13','3255'),(1241,'*4E2','tcp','192.168.10.247:50795','17.57.145.149:5223','17.57.145.149:5223','192.168.1.100:50795','4934','12','19','9739'),(1242,'*4E3','tcp','192.168.10.246:52653','52.98.84.114:443','52.98.84.114:443','192.168.1.100:52653','4906','8','11','2981'),(1243,'*4E4','tcp','192.168.10.245:55579','40.99.8.194:443','40.99.8.194:443','192.168.1.100:55579','6003','7','8','1250'),(1244,'*4E5','udp','192.168.10.254:49363','192.168.10.254:5247','192.168.10.254:5247','192.168.1.100:49363','987090490','724131','267584','43200097'),(1245,'*4E6','tcp','192.168.10.246:52457','52.98.65.2:443','52.98.65.2:443','192.168.1.100:52457','4904','8','10','2929'),(1246,'*4E7','tcp','192.168.10.246:52596','52.98.84.82:443','52.98.84.82:443','192.168.1.100:52596','4856','7','10','2929'),(1247,'*4E8','tcp','192.168.10.246:52632','17.57.145.138:5223','17.57.145.138:5223','192.168.1.100:52632','8225','39','42','10708'),(1248,'*4E9','tcp','192.168.10.247:49800','17.57.145.133:5223','17.57.145.133:5223','192.168.1.100:49800','4924','12','18','8235'),(1249,'*4EA','tcp','192.168.10.247:57404','34.120.31.60:443','34.120.31.60:443','192.168.1.100:57404','2000','12','13','3264'),(1250,'*4EB','tcp','192.168.10.246:51636','23.220.184.25:443','23.220.184.25:443','192.168.1.100:51636','9395','14','14','1660'),(1251,'*4EC','tcp','192.168.10.247:50571','17.57.145.132:5223','17.57.145.132:5223','192.168.1.100:50571','6071','19','25','8660'),(1252,'*4ED','tcp','192.168.10.246:51704','23.220.184.25:443','23.220.184.25:443','192.168.1.100:51704','9394','14','13','1608'),(1253,'*4EE','tcp','192.168.10.246:54508','40.99.10.98:443','40.99.10.98:443','192.168.1.100:54508','4968','9','12','3203'),(1254,'*4EF','tcp','192.168.10.246:52562','52.98.40.34:443','52.98.40.34:443','192.168.1.100:52562','4853','7','10','2752'),(1255,'*4F0','tcp','192.168.10.247:51081','17.57.145.137:5223','17.57.145.137:5223','192.168.1.100:51081','4975','13','20','8339'),(1256,'*4F1','tcp','192.168.10.246:54503','23.194.59.30:443','23.194.59.30:443','192.168.1.100:54503','9395','14','12','1556'),(1257,'*4F2','tcp','192.168.10.246:54551','17.57.145.54:5223','17.57.145.54:5223','192.168.1.100:54551','4975','13','19','9221'),(1258,'*4F3','tcp','192.168.10.247:57363','34.117.4.5:443','34.117.4.5:443','192.168.1.100:57363','69217','241','191','101153'),(1259,'*4F4','tcp','192.168.10.246:54615','40.99.10.98:443','40.99.10.98:443','192.168.1.100:54615','4852','7','11','2981'),(1260,'*4F5','tcp','192.168.10.247:49805','23.220.185.207:443','23.220.185.207:443','192.168.1.100:49805','7382','12','13','1546'),(1261,'*4F6','tcp','192.168.10.246:52627','17.57.145.135:5223','17.57.145.135:5223','192.168.1.100:52627','6876','27','32','10049'),(1262,'*4F7','tcp','192.168.10.247:49694','17.57.145.148:5223','17.57.145.148:5223','192.168.1.100:49694','4974','13','20','8339'),(1263,'*4F8','tcp','192.168.10.250:54445','23.74.229.83:443','23.74.229.83:443','192.168.1.100:54445','7672','11','8','1008'),(1264,'*4F9','tcp','192.168.10.247:51067','17.57.145.55:5223','17.57.145.55:5223','192.168.1.100:51067','4976','13','19','8288'),(1265,'*4FA','tcp','192.168.10.246:52675','17.57.145.138:5223','17.57.145.138:5223','192.168.1.100:52675','5605','18','25','9605'),(1266,'*4FB','tcp','192.168.10.247:49787','17.57.145.55:5223','17.57.145.55:5223','192.168.1.100:49787','4975','13','18','8236'),(1267,'*4FC','tcp','192.168.10.246:54644','52.98.65.2:443','52.98.65.2:443','192.168.1.100:54644','4968','9','12','3191'),(1268,'*4FD','tcp','192.168.10.246:54635','17.57.145.138:5223','17.57.145.138:5223','192.168.1.100:54635','5555','17','25','9603'),(1269,'*501','tcp','192.168.1.112:57129','192.168.1.100:8728','192.168.1.100:8728','192.168.1.112:57129','39837','38','21','1000'),(1270,'*502','udp','192.168.1.112:137','192.168.1.255:137','192.168.1.255:137','192.168.1.112:137','0','0','3','234');
/*!40000 ALTER TABLE `network_connection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_dhcpclient`
--

DROP TABLE IF EXISTS `network_dhcpclient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_dhcpclient` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dhcp_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `interface` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `status` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `address` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `route` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `dns` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `ntp` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_dhcpclient`
--

LOCK TABLES `network_dhcpclient` WRITE;
/*!40000 ALTER TABLE `network_dhcpclient` DISABLE KEYS */;
INSERT INTO `network_dhcpclient` VALUES (28,'*1','ether1','bound','192.168.1.100/24','True','True','True');
/*!40000 ALTER TABLE `network_dhcpclient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_dhcpclienttype`
--

DROP TABLE IF EXISTS `network_dhcpclienttype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_dhcpclienttype` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_dhcpclienttype`
--

LOCK TABLES `network_dhcpclienttype` WRITE;
/*!40000 ALTER TABLE `network_dhcpclienttype` DISABLE KEYS */;
INSERT INTO `network_dhcpclienttype` VALUES (1,'yes'),(2,'special classless'),(3,'no');
/*!40000 ALTER TABLE `network_dhcpclienttype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_dhcplease`
--

DROP TABLE IF EXISTS `network_dhcplease`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_dhcplease` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dhcp_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `address` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `mac_address` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `client` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `status` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `dhcpserver` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_dhcplease`
--

LOCK TABLES `network_dhcplease` WRITE;
/*!40000 ALTER TABLE `network_dhcplease` DISABLE KEYS */;
INSERT INTO `network_dhcplease` VALUES (9,'*2C9','192.168.10.246','92:AD:87:70:21:85','1:92:ad:87:70:21:85','bound','dhcp1'),(10,'*2CA','192.168.10.247','A2:45:D4:08:FD:77','1:a2:45:d4:8:fd:77','bound','dhcp1');
/*!40000 ALTER TABLE `network_dhcplease` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_dhcpnetwork`
--

DROP TABLE IF EXISTS `network_dhcpnetwork`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_dhcpnetwork` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dhcp_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `address` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `gateway` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `dns` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_dhcpnetwork`
--

LOCK TABLES `network_dhcpnetwork` WRITE;
/*!40000 ALTER TABLE `network_dhcpnetwork` DISABLE KEYS */;
INSERT INTO `network_dhcpnetwork` VALUES (12,'*1','192.168.10.0/24','192.168.10.254',''),(13,'*3','192.168.30.0/24','192.168.30.254',''),(15,'*8','192.168.60.0/24','192.168.60.254','8.8.8.8'),(16,'*2','192.168.99.0/24','192.168.99.254','');
/*!40000 ALTER TABLE `network_dhcpnetwork` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_dhcpserver`
--

DROP TABLE IF EXISTS `network_dhcpserver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_dhcpserver` (
  `id` int NOT NULL AUTO_INCREMENT,
  `dhcp_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `name` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `interface` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `address_pool` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_dhcpserver`
--

LOCK TABLES `network_dhcpserver` WRITE;
/*!40000 ALTER TABLE `network_dhcpserver` DISABLE KEYS */;
INSERT INTO `network_dhcpserver` VALUES (21,'*3','dhcp1','VLAN_10','dhcp_pool3'),(22,'*4','dhcp2','LAN','dhcp_pool6'),(23,'*5','dhcp3','VLAN_20','dhcp_pool7');
/*!40000 ALTER TABLE `network_dhcpserver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_dns`
--

DROP TABLE IF EXISTS `network_dns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_dns` (
  `id` int NOT NULL AUTO_INCREMENT,
  `server` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `dynamic` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `allow` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_dns`
--

LOCK TABLES `network_dns` WRITE;
/*!40000 ALTER TABLE `network_dns` DISABLE KEYS */;
INSERT INTO `network_dns` VALUES (6,'8.8.8.8,8.8.4.4','115.178.58.10,115.178.58.26,192.168.1.1','True');
/*!40000 ALTER TABLE `network_dns` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_ethernet`
--

DROP TABLE IF EXISTS `network_ethernet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_ethernet` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ether_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `ether_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `mac_address` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `ether_default` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_ethernet`
--

LOCK TABLES `network_ethernet` WRITE;
/*!40000 ALTER TABLE `network_ethernet` DISABLE KEYS */;
INSERT INTO `network_ethernet` VALUES (21,'*2','ether1','08:55:31:84:44:C4','ether1'),(22,'*3','ether2','08:55:31:84:44:C5','ether2'),(23,'*4','ether3','08:55:31:84:44:C6','ether3'),(24,'*5','ether4','08:55:31:84:44:C7','ether4');
/*!40000 ALTER TABLE `network_ethernet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_host`
--

DROP TABLE IF EXISTS `network_host`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_host` (
  `id` int NOT NULL AUTO_INCREMENT,
  `host_mac_address` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `host_address` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `host_server` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_host`
--

LOCK TABLES `network_host` WRITE;
/*!40000 ALTER TABLE `network_host` DISABLE KEYS */;
/*!40000 ALTER TABLE `network_host` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_identity`
--

DROP TABLE IF EXISTS `network_identity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_identity` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `name` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_identity`
--

LOCK TABLES `network_identity` WRITE;
/*!40000 ALTER TABLE `network_identity` DISABLE KEYS */;
INSERT INTO `network_identity` VALUES (19,'','mikrotik');
/*!40000 ALTER TABLE `network_identity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_interface`
--

DROP TABLE IF EXISTS `network_interface`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_interface` (
  `id` int NOT NULL AUTO_INCREMENT,
  `interface_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `interface_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `typeinterface` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `actualmtu` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `l2mtu` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=249 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_interface`
--

LOCK TABLES `network_interface` WRITE;
/*!40000 ALTER TABLE `network_interface` DISABLE KEYS */;
INSERT INTO `network_interface` VALUES (235,'*2','ether1','ether','1500','1598'),(236,'*3','ether2','ether','1500','1598'),(237,'*4','ether3','ether','1500','1598'),(238,'*5','ether4','ether','1500','1598'),(239,'*6','pwr-line1','ether','1500','1598'),(240,'*1','wlan1','wlan','1500','1600'),(241,'*83','LAN','bridge','1500','1598'),(242,'*7C','MAN12','bridge','1500','65535'),(243,'*A','VLAN_10','vlan','1500','1594'),(244,'*86','VLAN_20','vlan','1500','1594'),(245,'*6E','WAN','bridge','1500','65535'),(246,'*7B','arm159439','bridge','1500','65535'),(247,'*8A','mikrotik-1','cap','1500','1600'),(248,'*7F','tot123','bridge','1500','65535');
/*!40000 ALTER TABLE `network_interface` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_ipaddress`
--

DROP TABLE IF EXISTS `network_ipaddress`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_ipaddress` (
  `id` int NOT NULL AUTO_INCREMENT,
  `address_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `address` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `network` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `interface` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `dynamic` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_ipaddress`
--

LOCK TABLES `network_ipaddress` WRITE;
/*!40000 ALTER TABLE `network_ipaddress` DISABLE KEYS */;
INSERT INTO `network_ipaddress` VALUES (26,'*5','192.168.99.254/24','192.168.99.0','LAN','False'),(27,'*9','192.168.10.254/24','192.168.10.0','VLAN_10','False'),(28,'*A','192.168.1.100/24','192.168.1.0','ether1','True'),(29,'*B','192.168.20.254/24','192.168.20.0','VLAN_20','False');
/*!40000 ALTER TABLE `network_ipaddress` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_pool`
--

DROP TABLE IF EXISTS `network_pool`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_pool` (
  `id` int NOT NULL AUTO_INCREMENT,
  `pool_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `pool_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `pool_address` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_pool`
--

LOCK TABLES `network_pool` WRITE;
/*!40000 ALTER TABLE `network_pool` DISABLE KEYS */;
INSERT INTO `network_pool` VALUES (29,'*4','dhcp_pool3','192.168.10.1-192.168.10.253'),(30,'*7','dhcp_pool6','192.168.99.1-192.168.99.253'),(31,'*8','dhcp_pool7','192.168.20.1-192.168.20.253'),(32,'*9','pool6','192.168.20.1-192.168.20.100');
/*!40000 ALTER TABLE `network_pool` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_port`
--

DROP TABLE IF EXISTS `network_port`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_port` (
  `id` int NOT NULL AUTO_INCREMENT,
  `port_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `interface` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `bridge` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `pvid` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `frametypes` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=266 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_port`
--

LOCK TABLES `network_port` WRITE;
/*!40000 ALTER TABLE `network_port` DISABLE KEYS */;
INSERT INTO `network_port` VALUES (261,'*4','wlan1','LAN','10','admit-all'),(262,'*5','ether4','LAN','1','admit-all'),(263,'*6','ether2','LAN','1','admit-all'),(264,'*10','armmeyou-1','LAN','10','admit-all');
/*!40000 ALTER TABLE `network_port` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_route`
--

DROP TABLE IF EXISTS `network_route`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_route` (
  `id` int NOT NULL AUTO_INCREMENT,
  `route_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `dst_address` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `gateway` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `status` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `distance` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `dynamic` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=364 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_route`
--

LOCK TABLES `network_route` WRITE;
/*!40000 ALTER TABLE `network_route` DISABLE KEYS */;
INSERT INTO `network_route` VALUES (359,'*30000001','0.0.0.0/0','192.168.1.1','192.168.1.1 reachable via  ether1','1','True'),(360,'*4016A181','192.168.1.0/24','ether1','ether1 reachable','0','True'),(361,'*40169FCB','192.168.10.0/24','VLAN_10','VLAN_10 reachable','0','True'),(362,'*4016B7CF','192.168.20.0/24','VLAN_20','VLAN_20 reachable','0','True'),(363,'*401689D7','192.168.99.0/24','LAN','LAN reachable','0','True');
/*!40000 ALTER TABLE `network_route` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_server`
--

DROP TABLE IF EXISTS `network_server`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_server` (
  `id` int NOT NULL AUTO_INCREMENT,
  `server_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `server_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `server_interface` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `server_pool` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `server_profile` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_server`
--

LOCK TABLES `network_server` WRITE;
/*!40000 ALTER TABLE `network_server` DISABLE KEYS */;
INSERT INTO `network_server` VALUES (13,'*2','server1','VLAN_20','dhcp_pool7','hsprof12'),(14,'*2','server1','VLAN_20','dhcp_pool7','hsprof12'),(15,'*2','server1','VLAN_20','dhcp_pool7','hsprof12'),(16,'*2','server1','VLAN_20','dhcp_pool7','hsprof12');
/*!40000 ALTER TABLE `network_server` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_serverprofile`
--

DROP TABLE IF EXISTS `network_serverprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_serverprofile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ser_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `ser_address` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `ser_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `ser_dns` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=70 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_serverprofile`
--

LOCK TABLES `network_serverprofile` WRITE;
/*!40000 ALTER TABLE `network_serverprofile` DISABLE KEYS */;
INSERT INTO `network_serverprofile` VALUES (68,'default','0.0.0.0','*0',''),(69,'hsprof12','192.168.20.254','*1','www.bandee.net');
/*!40000 ALTER TABLE `network_serverprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_user`
--

DROP TABLE IF EXISTS `network_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `name` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `group` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=94 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_user`
--

LOCK TABLES `network_user` WRITE;
/*!40000 ALTER TABLE `network_user` DISABLE KEYS */;
INSERT INTO `network_user` VALUES (91,'*1','admin','full'),(92,'*2','user1','full'),(93,'*4','user2','full');
/*!40000 ALTER TABLE `network_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_userprofile`
--

DROP TABLE IF EXISTS `network_userprofile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_userprofile` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userpro_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `userpro_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `userpro_address` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `userpro_share` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `userpro_rate` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=250 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_userprofile`
--

LOCK TABLES `network_userprofile` WRITE;
/*!40000 ALTER TABLE `network_userprofile` DISABLE KEYS */;
INSERT INTO `network_userprofile` VALUES (247,'*0','default','','1',''),(248,'*1','uprof1','','1','500k/500k'),(249,'*2','aaa','dhcp_pool7','2','500k/500k');
/*!40000 ALTER TABLE `network_userprofile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_users`
--

DROP TABLE IF EXISTS `network_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `user_ser` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `user_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `user_pass` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `user_pro` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=155 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_users`
--

LOCK TABLES `network_users` WRITE;
/*!40000 ALTER TABLE `network_users` DISABLE KEYS */;
INSERT INTO `network_users` VALUES (148,'*0','','default-trial','',''),(149,'*1','all','admin','123','default'),(150,'*2','server1','admin1','1234','default'),(151,'*3','all','user3','123','default'),(152,'*4','all','user4','159','default'),(153,'*5','all','user5','159','default'),(154,'*7','all','user6','','default');
/*!40000 ALTER TABLE `network_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_vlan`
--

DROP TABLE IF EXISTS `network_vlan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_vlan` (
  `id` int NOT NULL AUTO_INCREMENT,
  `vlanid` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `vlan_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `vlan_id` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `vlan_interface` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `vlan_type` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_vlan`
--

LOCK TABLES `network_vlan` WRITE;
/*!40000 ALTER TABLE `network_vlan` DISABLE KEYS */;
INSERT INTO `network_vlan` VALUES (48,'*A','VLAN_10','10','LAN','vlan'),(49,'*86','VLAN_20','20','LAN','vlan');
/*!40000 ALTER TABLE `network_vlan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `network_vlans`
--

DROP TABLE IF EXISTS `network_vlans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `network_vlans` (
  `id` int NOT NULL AUTO_INCREMENT,
  `vlansid` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `vlans_bridge` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `vlans_ids` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `tagged` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `untagged` varchar(45) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=63 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `network_vlans`
--

LOCK TABLES `network_vlans` WRITE;
/*!40000 ALTER TABLE `network_vlans` DISABLE KEYS */;
INSERT INTO `network_vlans` VALUES (60,'*2','LAN','10,1','LAN,wlan1',''),(61,'*7','tot123','1','','');
/*!40000 ALTER TABLE `network_vlans` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-17 14:29:54
