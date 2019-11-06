-- MySQL dump 10.13  Distrib 8.0.18, for macos10.14 (x86_64)
--
-- Host: localhost    Database: elec9609
-- ------------------------------------------------------
-- Server version	5.7.27-log

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
-- Table structure for table `goods_goodsbrand`
--

DROP TABLE IF EXISTS `goods_goodsbrand`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `goods_goodsbrand` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `desc` longtext NOT NULL,
  `image` varchar(200) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_goodsbrand_category_id_6fc84a73_fk_goods_goodscategory_id` (`category_id`),
  CONSTRAINT `goods_goodsbrand_category_id_6fc84a73_fk_goods_goodscategory_id` FOREIGN KEY (`category_id`) REFERENCES `goods_goodscategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_goodsbrand`
--

LOCK TABLES `goods_goodsbrand` WRITE;
/*!40000 ALTER TABLE `goods_goodsbrand` DISABLE KEYS */;
INSERT INTO `goods_goodsbrand` VALUES (1,'mfw','mfw','brands/1_OWrH4TR.jpg','2019-10-31 13:08:41.000000',1),(2,'chanel','Chanel','brands/7_TsObFoF.jpg','2019-10-31 13:08:58.000000',1),(3,'allwouldenvy','allwouldenvy','brands/4_SleThUi.jpg','2019-10-31 13:09:18.000000',1),(4,'love&bravery','love&bravery','brands/3_lA1NpgZ.jpg','2019-10-31 13:09:31.000000',13),(5,'zara','zara','brands/5_kSYZgIT.jpg','2019-10-31 13:09:46.000000',13),(6,'H&M','H&M','brands/6_W9I55Da.jpg','2019-10-31 13:10:01.000000',13),(7,'kissablebella','kissablebella','brands/2_2UTmDtk.jpg','2019-10-31 13:10:15.000000',19),(8,'burberry','burberry','brands/13.jpg','2019-10-31 13:10:27.000000',19),(9,'miumiu','miumiu','brands/10_JuyH7ra.jpg','2019-10-31 13:10:51.000000',19);
/*!40000 ALTER TABLE `goods_goodsbrand` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-01  0:48:53
