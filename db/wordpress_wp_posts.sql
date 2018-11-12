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
-- Table structure for table `wp_posts`
--

DROP TABLE IF EXISTS `wp_posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wp_posts` (
  `ID` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `post_author` bigint(20) unsigned NOT NULL DEFAULT '0',
  `post_date` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `post_date_gmt` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `post_content` longtext NOT NULL,
  `post_title` text NOT NULL,
  `post_excerpt` text NOT NULL,
  `post_status` varchar(20) NOT NULL DEFAULT 'publish',
  `comment_status` varchar(20) NOT NULL DEFAULT 'open',
  `ping_status` varchar(20) NOT NULL DEFAULT 'open',
  `post_password` varchar(20) NOT NULL DEFAULT '',
  `post_name` varchar(200) NOT NULL DEFAULT '',
  `to_ping` text NOT NULL,
  `pinged` text NOT NULL,
  `post_modified` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `post_modified_gmt` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `post_content_filtered` longtext NOT NULL,
  `post_parent` bigint(20) unsigned NOT NULL DEFAULT '0',
  `guid` varchar(255) NOT NULL DEFAULT '',
  `menu_order` int(11) NOT NULL DEFAULT '0',
  `post_type` varchar(20) NOT NULL DEFAULT 'post',
  `post_mime_type` varchar(100) NOT NULL DEFAULT '',
  `comment_count` bigint(20) NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID`),
  KEY `post_name` (`post_name`),
  KEY `type_status_date` (`post_type`,`post_status`,`post_date`,`ID`),
  KEY `post_parent` (`post_parent`),
  KEY `post_author` (`post_author`)
) ENGINE=InnoDB AUTO_INCREMENT=237 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wp_posts`
--

LOCK TABLES `wp_posts` WRITE;
/*!40000 ALTER TABLE `wp_posts` DISABLE KEYS */;
INSERT INTO `wp_posts` VALUES (1,1,'2018-09-28 16:29:45','2018-09-28 16:29:45','Welcome to WordPress. This is your first post. Edit or delete it, then start blogging!','Hello world!','','publish','open','open','','hello-world','','','2018-09-28 16:29:45','2018-09-28 16:29:45','',0,'http://localhost/wordpress3_9/?p=1',0,'post','',1),(2,1,'2018-09-28 16:29:45','2018-09-28 16:29:45','This is an example page. It\'s different from a blog post because it will stay in one place and will show up in your site navigation (in most themes). Most people start with an About page that introduces them to potential site visitors. It might say something like this:\n\n<blockquote>Hi there! I\'m a bike messenger by day, aspiring actor by night, and this is my blog. I live in Los Angeles, have a great dog named Jack, and I like pi&#241;a coladas. (And gettin\' caught in the rain.)</blockquote>\n\n...or something like this:\n\n<blockquote>The XYZ Doohickey Company was founded in 1971, and has been providing quality doohickeys to the public ever since. Located in Gotham City, XYZ employs over 2,000 people and does all kinds of awesome things for the Gotham community.</blockquote>\n\nAs a new WordPress user, you should go to <a href=\"http://localhost/wordpress3_9/wp-admin/\">your dashboard</a> to delete this page and create new pages for your content. Have fun!','Sample Page','','publish','open','open','','sample-page','','','2018-09-28 16:29:45','2018-09-28 16:29:45','',0,'http://localhost/wordpress3_9/?page_id=2',0,'page','',0),(4,1,'2018-10-01 21:05:54','2018-10-01 21:05:54','<i>999</i>','123','','publish','open','open','','123','','','2018-10-01 21:05:54','2018-10-01 21:05:54','',0,'http://localhost/wordpress3_9/?p=4',0,'post','',0),(5,1,'2018-10-01 21:03:51','2018-10-01 21:03:51','&lt;em&gt;as&lt;/em&gt;\r\n\r\n&lt;i&gt;123&lt;/i&gt;','','','inherit','open','open','','4-revision-v1','','','2018-10-01 21:03:51','2018-10-01 21:03:51','',4,'http://localhost/wordpress3_9/?p=5',0,'revision','',0),(6,1,'2018-10-01 21:04:12','2018-10-01 21:04:12','&lt;em&gt;as&lt;/em&gt;\r\n\r\n&lt;i&gt;123&lt;/i&gt;','123','','inherit','open','open','','4-revision-v1','','','2018-10-01 21:04:12','2018-10-01 21:04:12','',4,'http://localhost/wordpress3_9/?p=6',0,'revision','',0),(7,1,'2018-10-01 21:04:55','2018-10-01 21:04:55','<i>999</i>','123','','inherit','open','open','','4-revision-v1','','','2018-10-01 21:04:55','2018-10-01 21:04:55','',4,'http://localhost/wordpress3_9/?p=7',0,'revision','',0),(82,1,'2018-10-12 13:17:38','2018-10-12 13:17:38','Traceback test','Traceback test','','publish','open','open','','traceback-test','','\nhttp://localhost/wordpress3_9/?p=1','2018-10-12 13:17:38','2018-10-12 13:17:38','',0,'http://localhost/wordpress3_9/?p=82',0,'post','',1),(83,1,'2018-10-12 13:17:32','2018-10-12 13:17:32','Traceback test','Traceback test','','inherit','open','open','','82-revision-v1','','','2018-10-12 13:17:32','2018-10-12 13:17:32','',82,'http://localhost/wordpress3_9/?p=83',0,'revision','',0),(149,1,'2018-10-29 14:56:37','0000-00-00 00:00:00','','Home','','draft','open','open','','','','','2018-10-29 14:56:37','0000-00-00 00:00:00','',0,'http://localhost/wordpress3_9/?p=149',1,'nav_menu_item','',0),(150,1,'2018-10-29 14:56:37','0000-00-00 00:00:00',' ','','','draft','open','open','','','','','2018-10-29 14:56:37','0000-00-00 00:00:00','',0,'http://localhost/wordpress3_9/?p=150',1,'nav_menu_item','',0),(151,1,'2018-10-29 15:06:12','0000-00-00 00:00:00','','Home','','draft','open','open','','','','','2018-10-29 15:06:12','0000-00-00 00:00:00','',0,'http://localhost/wordpress3_9/?p=151',1,'nav_menu_item','',0),(152,1,'2018-10-29 15:06:12','0000-00-00 00:00:00',' ','','','draft','open','open','','','','','2018-10-29 15:06:12','0000-00-00 00:00:00','',0,'http://localhost/wordpress3_9/?p=152',1,'nav_menu_item','',0),(182,1,'2018-11-07 01:27:46','0000-00-00 00:00:00','','Auto Draft','','auto-draft','open','open','','','','','2018-11-07 01:27:46','0000-00-00 00:00:00','',0,'http://localhost/wordpress3_9/?p=182',0,'post','',0),(194,1,'2018-11-07 04:32:13','0000-00-00 00:00:00','','Auto Draft','','auto-draft','open','open','','','','','2018-11-07 04:32:13','0000-00-00 00:00:00','',0,'http://localhost/wordpress3_9/?p=194',0,'post','',0),(221,1,'2018-11-08 14:42:12','2018-11-08 14:42:12','','leaf','','inherit','open','open','','leaf','','','2018-11-08 14:42:12','2018-11-08 14:42:12','',0,'http://localhost/wordpress3_9/wp-content/uploads/2018/11/leaf.png',0,'attachment','image/png',0),(236,1,'2018-11-12 16:29:24','0000-00-00 00:00:00','','Auto Draft','','auto-draft','open','open','','','','','2018-11-12 16:29:24','0000-00-00 00:00:00','',0,'http://localhost/wordpress3_9/?p=236',0,'post','',0);
/*!40000 ALTER TABLE `wp_posts` ENABLE KEYS */;
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
