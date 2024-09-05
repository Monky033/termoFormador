use Juani;

INSERT INTO Maquinas (nombre, temperatura_ambiente, temperatura_optima, material_disponible)
VALUES ('Maquina A', 25.00, 120.00, 1000),
       ('Maquina B', 25.00, 125.00, 800),
       ('Maquina C', 25.00, 130.00, 1200),
       ('Maquina D', 25.00, 110.00, 1500),
       ('Maquina E', 25.00, 115.00, 500);
       
       
INSERT INTO Operaciones (maquina_id, tipo_operacion, cantidad, fecha_operacion)
VALUES 
(1, 'Calentar', 30, '2024-08-30 08:00:00'),
(1, 'Formar', 200, '2024-08-30 09:00:00'),
(2, 'Calentar', 50, '2024-08-30 08:30:00'),
(2, 'Formar', 300, '2024-08-30 09:30:00'),
(3, 'Enfriar', 10, '2024-08-30 10:00:00'),
(3, 'Formar', 100, '2024-08-30 11:00:00'),
(4, 'Calentar', 45, '2024-08-30 08:15:00'),
(4, 'Enfriar', 20, '2024-08-30 10:30:00'),
(5, 'Formar', 150, '2024-08-30 09:45:00'),
(5, 'Enfriar', 15, '2024-08-30 11:15:00');

SELECT * FROM Maquinas;

SELECT * FROM Operaciones;

SELECT nombre FROM Maquinas WHERE material_disponible > 800;

SELECT * FROM Operaciones WHERE maquina_id = 3;


SELECT tipo_operacion, fecha_operacion 
FROM Operaciones 
JOIN Maquinas ON Operaciones.maquina_id = Maquinas.id 
WHERE Maquinas.nombre = 'Maquina A';
