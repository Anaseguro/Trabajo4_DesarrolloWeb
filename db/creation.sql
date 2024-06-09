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
INSERT INTO Ubicaciones(salas, descripcion, paciente, equipos) VALUES('Sala B', 'Descripción de sala B', 'Ana', 'Respirador');
INSERT INTO Ubicaciones(salas, descripcion, paciente, equipos) VALUES('Sala C', 'Descripción de sala C', 'Carlos', 'Electrocardiógrafo');
INSERT INTO Ubicaciones(salas, descripcion, paciente, equipos) VALUES('Sala D', 'Descripción de sala D', 'María', 'Desfibrilador');
INSERT INTO Ubicaciones(salas, descripcion, paciente, equipos) VALUES('Sala E', 'Descripción de sala E', 'Luis', 'Ultrasonido');
INSERT INTO Ubicaciones(salas, descripcion, paciente, equipos) VALUES('Sala F', 'Descripción de sala F', 'Sofía', 'Tomógrafo');

INSERT INTO Equipo(nombre_equipo, marca, descripcion, mantenimiento, fecha_mant) VALUES('Camilla', 'Siemens', 'Camilla para transporte de pacientes', 'Preventivo', '02-02-2020');
INSERT INTO Equipo(nombre_equipo, marca, descripcion, mantenimiento, fecha_mant) VALUES('Respirador', 'Philips', 'Respirador artificial', 'Correctivo', '15-03-2021');
INSERT INTO Equipo(nombre_equipo, marca, descripcion, mantenimiento, fecha_mant) VALUES('Monitor de signos vitales', 'GE', 'Monitor multiparamétrico', 'Preventivo', '20-05-2022');
INSERT INTO Equipo(nombre_equipo, marca, descripcion, mantenimiento, fecha_mant) VALUES('Desfibrilador', 'Zoll', 'Desfibrilador automático', 'Correctivo', '10-08-2021');
INSERT INTO Equipo(nombre_equipo, marca, descripcion, mantenimiento, fecha_mant) VALUES('Electrocardiógrafo', 'Mindray', 'Electrocardiógrafo de 12 derivaciones', 'Preventivo', '05-11-2023');
INSERT INTO Equipo(nombre_equipo, marca, descripcion, mantenimiento, fecha_mant) VALUES('Ultrasonido', 'Samsung', 'Equipo de ultrasonido', 'Correctivo', '25-01-2022');

INSERT INTO users(nombre, apellido, sintomas, ubicacion, medico, equipo) VALUES('Juan', 'Fernandez', 'Operación', 'Sala A', 'Mario', 'Respirador');
INSERT INTO users(nombre, apellido, sintomas, ubicacion, medico, equipo) VALUES('Ana', 'Gomez', 'Chequeo', 'Sala B', 'Laura', 'Monitor de signos vitales');
INSERT INTO users(nombre, apellido, sintomas, ubicacion, medico, equipo) VALUES('Carlos', 'Perez', 'Consulta', 'Sala C', 'Pedro', 'Electrocardiógrafo');
INSERT INTO users(nombre, apellido, sintomas, ubicacion, medico, equipo) VALUES('María', 'Rodriguez', 'Revisión', 'Sala D', 'Ana', 'Desfibrilador');
INSERT INTO users(nombre, apellido, sintomas, ubicacion, medico, equipo) VALUES('Luis', 'Martinez', 'Emergencia', 'Sala E', 'Juan', 'Ultrasonido');
INSERT INTO users(nombre, apellido, sintomas, ubicacion, medico, equipo) VALUES('Sofía', 'Ramirez', 'Tratamiento', 'Sala F', 'Claudia', 'Tomógrafo');
