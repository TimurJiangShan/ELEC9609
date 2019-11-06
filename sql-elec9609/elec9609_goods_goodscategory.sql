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
-- Table structure for table `goods_goodscategory`
--

DROP TABLE IF EXISTS `goods_goodscategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `goods_goodscategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `code` varchar(30) NOT NULL,
  `desc` longtext NOT NULL,
  `category_type` int(11) NOT NULL,
  `is_tab` tinyint(1) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `parent_category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `goods_goodscategory_parent_category_id_ccec2509_fk_goods_goo` (`parent_category_id`),
  CONSTRAINT `goods_goodscategory_parent_category_id_ccec2509_fk_goods_goo` FOREIGN KEY (`parent_category_id`) REFERENCES `goods_goodscategory` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_goodscategory`
--

LOCK TABLES `goods_goodscategory` WRITE;
/*!40000 ALTER TABLE `goods_goodscategory` DISABLE KEYS */;
INSERT INTO `goods_goodscategory` VALUES (1,'Clothing','cl','Clothing',1,1,'2019-10-31 13:06:41.000000',NULL),(2,'J & R','jr','',2,0,'2019-10-31 13:06:41.579179',1),(3,'J & R','jr2','',3,0,'2019-10-31 13:06:41.594755',2),(4,'Bottoms','bo','',2,0,'2019-10-31 13:06:41.605438',1),(5,'Shorts','sh','',3,0,'2019-10-31 13:06:41.619949',4),(6,'Dresses','dr','',3,0,'2019-10-31 13:06:41.634471',4),(7,'Skirt','sk','',3,0,'2019-10-31 13:06:41.646792',4),(8,'Tops','tp','',2,0,'2019-10-31 13:06:41.667057',1),(9,'Blouse','bl','',3,0,'2019-10-31 13:06:41.678705',8),(10,'Knit','kn','',3,0,'2019-10-31 13:06:41.694599',8),(11,'Embroidered','em','',3,0,'2019-10-31 13:06:41.710628',8),(12,'Sleeveless','sl','',3,0,'2019-10-31 13:06:41.722376',8),(13,'Shoes','ho','Shoes',1,1,'2019-10-31 13:06:41.000000',NULL),(14,'Sandals','sa','',2,0,'2019-10-31 13:06:41.746162',13),(15,'Heels','he','',3,0,'2019-10-31 13:06:41.759014',14),(16,'Flats','fl','',3,0,'2019-10-31 13:06:41.770621',14),(17,'Mules','mu','',2,0,'2019-10-31 13:06:41.785089',13),(18,'Mules','mu','',3,0,'2019-10-31 13:06:41.798651',17),(19,'Others','ot','Others',1,1,'2019-10-31 13:06:41.000000',NULL),(20,'Sports','sp','',2,0,'2019-10-31 13:06:41.820956',19),(21,'Sports-tights','st','',3,0,'2019-10-31 13:06:41.833870',20),(22,'Sports-bras','sb','',3,0,'2019-10-31 13:06:41.844692',20),(23,'Accessories','ac','',2,0,'2019-10-31 13:06:41.855878',19),(24,'Bags','ba','',3,0,'2019-10-31 13:06:41.866768',23);
/*!40000 ALTER TABLE `goods_goodscategory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-01 15:13:30
