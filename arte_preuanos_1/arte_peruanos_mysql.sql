/*
SQLyog Ultimate v11.33 (64 bit)
MySQL - 10.4.32-MariaDB : Database - artes_peruanos
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`artes_peruanos` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;

USE `artes_peruanos`;

/*Table structure for table `cartera` */

DROP TABLE IF EXISTS `cartera`;

CREATE TABLE `cartera` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `tipo_id` int(11) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `tipo_id` (`tipo_id`),
  CONSTRAINT `cartera_ibfk_1` FOREIGN KEY (`tipo_id`) REFERENCES `tipocartera` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*Data for the table `cartera` */

insert  into `cartera`(`id`,`nombre`,`tipo_id`,`precio`,`fecha_registro`) values (1,'Cartera de cuero',1,'40.00','2025-05-29'),(2,'Cartera de cuero',1,'40.00','2025-05-29'),(3,'Cartera de piel de oveja',3,'190.00','2025-05-30'),(4,'Cartera de lana',4,'80.00','2025-05-28'),(5,'Cartera de tela',1,'30.00','2025-05-30'),(6,'Cartera de plastico ',1,'340.00','2025-05-30');

/*Table structure for table `tipocartera` */

DROP TABLE IF EXISTS `tipocartera`;

CREATE TABLE `tipocartera` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*Data for the table `tipocartera` */

insert  into `tipocartera`(`id`,`nombre`) values (1,'Tradicional'),(2,'Selvático'),(3,'Andino'),(4,'Costeño');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
