CREATE DATABASE  IF NOT EXISTS `wordpress` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;
USE `wordpress`;
-- MySQL dump 10.13  Distrib 5.7.17, for macos10.12 (x86_64)
--
-- Host: localhost    Database: wordpress
-- ------------------------------------------------------
-- Server version	5.7.20

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
-- Table structure for table `wp_postmeta`
--

DROP TABLE IF EXISTS `wp_postmeta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wp_postmeta` (
  `meta_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `post_id` bigint(20) unsigned NOT NULL DEFAULT '0',
  `meta_key` varchar(255) DEFAULT NULL,
  `meta_value` longtext,
  PRIMARY KEY (`meta_id`),
  KEY `post_id` (`post_id`),
  KEY `meta_key` (`meta_key`)
) ENGINE=InnoDB AUTO_INCREMENT=326 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_postmeta`
--

LOCK TABLES `wp_postmeta` WRITE;
/*!40000 ALTER TABLE `wp_postmeta` DISABLE KEYS */;
INSERT INTO `wp_postmeta` VALUES (1,2,'_wp_page_template','default'),(2,4,'_edit_last','1'),(3,4,'_edit_lock','1538427954:1'),(37,82,'_edit_last','1'),(38,82,'_edit_lock','1541685423:1'),(104,149,'_menu_item_type','custom'),(105,149,'_menu_item_menu_item_parent','0'),(106,149,'_menu_item_object_id','149'),(107,149,'_menu_item_object','custom'),(108,149,'_menu_item_target',''),(109,149,'_menu_item_classes','a:1:{i:0;s:0:\"\";}'),(110,149,'_menu_item_xfn',''),(111,149,'_menu_item_url','http://localhost/wordpress3_9/'),(112,149,'_menu_item_orphaned','1540824997'),(113,150,'_menu_item_type','post_type'),(114,150,'_menu_item_menu_item_parent','0'),(115,150,'_menu_item_object_id','2'),(116,150,'_menu_item_object','page'),(117,150,'_menu_item_target',''),(118,150,'_menu_item_classes','a:1:{i:0;s:0:\"\";}'),(119,150,'_menu_item_xfn',''),(120,150,'_menu_item_url',''),(121,150,'_menu_item_orphaned','1540824997'),(123,151,'_menu_item_type','custom'),(124,151,'_menu_item_menu_item_parent','0'),(125,151,'_menu_item_object_id','151'),(126,151,'_menu_item_object','custom'),(127,151,'_menu_item_target',''),(128,151,'_menu_item_classes','a:1:{i:0;s:0:\"\";}'),(129,151,'_menu_item_xfn',''),(130,151,'_menu_item_url','http://localhost/wordpress3_9/'),(131,151,'_menu_item_orphaned','1540825572'),(132,152,'_menu_item_type','post_type'),(133,152,'_menu_item_menu_item_parent','0'),(134,152,'_menu_item_object_id','2'),(135,152,'_menu_item_object','page'),(136,152,'_menu_item_target',''),(137,152,'_menu_item_classes','a:1:{i:0;s:0:\"\";}'),(138,152,'_menu_item_xfn',''),(139,152,'_menu_item_url',''),(140,152,'_menu_item_orphaned','1540825572'),(194,1,'_edit_lock','1541109497:1'),(228,194,'_edit_lock','1541565209:1'),(289,221,'_wp_attached_file','2018/11/leaf.png'),(290,221,'_wp_attachment_metadata','a:5:{s:5:\"width\";i:612;s:6:\"height\";i:552;s:4:\"file\";s:16:\"2018/11/leaf.png\";s:5:\"sizes\";a:3:{s:9:\"thumbnail\";a:4:{s:4:\"file\";s:16:\"leaf-150x150.png\";s:5:\"width\";i:150;s:6:\"height\";i:150;s:9:\"mime-type\";s:9:\"image/png\";}s:6:\"medium\";a:4:{s:4:\"file\";s:16:\"leaf-400x360.png\";s:5:\"width\";i:400;s:6:\"height\";i:360;s:9:\"mime-type\";s:9:\"image/png\";}s:14:\"post-thumbnail\";a:4:{s:4:\"file\";s:16:\"leaf-612x198.png\";s:5:\"width\";i:612;s:6:\"height\";i:198;s:9:\"mime-type\";s:9:\"image/png\";}}s:10:\"image_meta\";a:10:{s:8:\"aperture\";i:0;s:6:\"credit\";s:0:\"\";s:6:\"camera\";s:0:\"\";s:7:\"caption\";s:0:\"\";s:17:\"created_timestamp\";i:0;s:9:\"copyright\";s:0:\"\";s:12:\"focal_length\";i:0;s:3:\"iso\";i:0;s:13:\"shutter_speed\";i:0;s:5:\"title\";s:0:\"\";}}');
/*!40000 ALTER TABLE `wp_postmeta` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-12 11:34:38
