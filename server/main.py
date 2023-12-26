# from controllers.compiler import *
import controllers.compiler.parser as parser


parser.parser.parse(
    '''
CREATE DATA BASE tbbanco;  
USE tbbanco;
CREATE TABLE tbestado (
idestado int PRIMARY KEY,
estado nvarchar(50) NOT NULL);

CREATE TABLE tbidentificaciontipo (
ididentificaciontipo int PRIMARY KEY,
identificaciontipo nvarchar(15) not null);

CREATE TABLE tbcliente (codigocliente nvarchar(15) PRIMARY KEY,
primer_nombre nvarchar(50) not null,
segundo_nombre nvarchar(50),
primer_apellido nvarchar(50) not null,
segundo_apellido nvarchar(50),
fecha_nacimiento date not null, 
genero nvarchar(1),
idestado int not null REFERENCE tbestado (idestado));

CREATE TABLE tbidentificacion (
ididentificacion int PRIMARY KEY,
codigocliente nvarchar(15) PRIMARY KEY REFERENCE tbcliente (codigocliente),
identificacion nvarchar(20) NOT NULL,
ididentificaciontipo int REFERENCE tbidentificaciontipo (ididentificaciontipo));

INSERT INTO tbidentificaciontipo (ididentificaciontipo,identificaciontipo) VALUES(1,'DPI');
INSERT INTO tbidentificaciontipo (ididentificaciontipo,identificaciontipo) VALUES(2,'NIT');
INSERT INTO tbidentificaciontipo (ididentificaciontipo,identificaciontipo) VALUES(3,'PASAPORTE');

INSERT INTO tbestado (idestado,estado) VALUES(1,'Activo');
INSERT INTO tbestado (idestado,estado) VALUES(2,'Inactivo');
INSERT INTO tbestado (idestado,estado) VALUES(3,'Eliminado');

INSERT INTO tbcliente (codigocliente,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,fecha_nacimiento,genero,idestado)
VALUES ('GT-0001','PETER','JUAN','PARKER','SEGUNDO','1990-01-01','M',1);
INSERT INTO tbcliente (codigocliente,primer_nombre,primer_apellido,segundo_apellido,fecha_nacimiento,idestado)
VALUES ('GT-0002','JULIO','PEREZ','LOPEZ','1995-12-01',1);

INSERT INTO tbidentificacion (ididentificacion,codigocliente,identificacion,ididentificaciontipo)
VALUES (1,'GT-0001','45784560101',1);
INSERT INTO tbidentificacion (ididentificacion,codigocliente,identificacion,ididentificaciontipo)
VALUES (2,'GT-0001','94675057',2);

INSERT INTO tbidentificacion (ididentificacion,codigocliente,identificacion,ididentificaciontipo)
VALUES (3,'GT-0002','4854560101',1);


CREATE TABLE tbproducto (idproducto int primary key,
producto nvarchar(100) not null,
idestado int not null);

INSERT INTO tbproducto (idproducto,producto,idestado) VALUES(1,'Credito Fiduiciario',1);
INSERT INTO tbproducto (idproducto,producto,idestado) VALUES(2,'Credito Hipotecario',1);
INSERT INTO tbproducto (idproducto,producto,idestado) VALUES(3,'Tarjeta de Credito Oro',1);


'''
)
