CREATE DATABASE IF NOT EXISTS gestion_prestamos;
USE gestion_prestamos;

-- Tablas  ->
CREATE TABLE usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(15)
);


CREATE TABLE libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(100),
    disponible BOOLEAN DEFAULT TRUE
);


CREATE TABLE prestamos (
    id_prestamo INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_libro INT,
    fecha_prestamo DATETIME DEFAULT CURRENT_TIMESTAMP,
    fecha_devolucion DATETIME NULL,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_libro) REFERENCES libros(id_libro)
);

-- Vistas  ->
CREATE VIEW vista_libros_disponibles AS
SELECT id_libro, titulo, autor
FROM libros
WHERE disponible = TRUE;

CREATE VIEW vista_prestamos_activos AS
SELECT p.id_prestamo, p.id_usuario, u.nombre AS usuario, l.titulo, p.fecha_prestamo, p.id_libro
FROM prestamos p
JOIN usuarios u ON p.id_usuario = u.id_usuario
JOIN libros l ON p.id_libro = l.id_libro
WHERE p.fecha_devolucion IS NULL;



CREATE VIEW vista_historial_prestamos AS
SELECT p.id_prestamo, u.id_usuario, u.nombre AS usuario, l.titulo, p.fecha_prestamo, p.fecha_devolucion, p.id_libro
FROM prestamos p
JOIN usuarios u ON p.id_usuario = u.id_usuario
JOIN libros l ON p.id_libro = l.id_libro;





-- Inserts  ->
INSERT INTO usuarios (nombre, correo, telefono) VALUES
('Juan Pérez', 'juan.perez@example.com', '50212345678'),
('María López', 'maria.lopez@example.com', '50287654321'),
('Carlos García', 'carlos.garcia@example.com', '50211223344'),
('Ana Fernández', 'ana.fernandez@example.com', '50255667788'),
('Luis Rodríguez', 'luis.rodriguez@example.com', '50299887766');


INSERT INTO libros (titulo, autor, disponible) VALUES
('Cien Años de Soledad', 'Gabriel García Márquez', TRUE),
('Don Quijote de la Mancha', 'Miguel de Cervantes', TRUE),
('El Amor en los Tiempos del Cólera', 'Gabriel García Márquez', TRUE),
('Crónica de una Muerte Anunciada', 'Gabriel García Márquez', TRUE),
('1984', 'George Orwell', TRUE),
('Rebelión en la Granja', 'George Orwell', TRUE),
('El Principito', 'Antoine de Saint-Exupéry', TRUE),
('Fahrenheit 451', 'Ray Bradbury', TRUE),
('La Sombra del Viento', 'Carlos Ruiz Zafón', TRUE),
('El Juego del Ángel', 'Carlos Ruiz Zafón', TRUE),
('Marina', 'Carlos Ruiz Zafón', TRUE),
('El Alquimista', 'Paulo Coelho', TRUE),
('Veronika Decide Morir', 'Paulo Coelho', TRUE),
('El Caballero de la Armadura Oxidada', 'Robert Fisher', TRUE),
('El Hobbit', 'J.R.R. Tolkien', TRUE);




