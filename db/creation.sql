SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

DROP TABLE IF EXISTS Ubicaciones ;
DROP TABLE IF EXISTS Equipo ;
DROP TABLE IF EXISTS users ;

CREATE TABLE IF NOT EXISTS Ubicaciones (
  id INT NOT NULL AUTO_INCREMENT,
  salas VARCHAR(255) NOT NULL,
  descripcion VARCHAR(255) NOT NULL,
  paciente VARCHAR(255) NOT NULL,
  equipos VARCHAR(255) NOT NULL,
  --description TEXT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS Equipo (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  marca VARCHAR(255) NOT NULL,
  descripcion VARCHAR(255) NOT NULL,
  mantenimiento VARCHAR(255) NOT NULL,
  fecha_mant VARCHAR(255) NOT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(255) NOT NULL,
  apellido VARCHAR(255) NOT NULL,
  sintomas VARCHAR(255) NOT NULL,
  ubicacion VARCHAR(255) NOT NULL,
  medico VARCHAR(255) NOT NULL,
  equipo VARCHAR(255) NOT NULL,
  PRIMARY KEY (id))
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;


INSERT INTO Ubicaciones(salas, descripcion, paciente, equipos) VALUES('Sala A', 'Esto es una descripción', 'Julio', 'Monitor de signos vitales');
INSERT INTO Equipo(nombre_equipo, marca, descripcion, mantenimiento, fecha_mant) VALUES('Camilla', 'Siemens', 'Camilla para transporte de pacientes', 'Preventivo', '02-02-2020');
INSERT INTO users(nombre, apellido, sintomas, ubicacion, medico, equipo) VALUES('Juan', 'Fernandez', 'Operación', 'Sala A', 'Mario', 'Respirador');