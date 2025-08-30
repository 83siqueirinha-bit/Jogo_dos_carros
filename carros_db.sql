-- Criando um banco de dados simples
CREATE DATABASE carros_db;

-- Usando esse banco criado
USE carros_db;

-- Criando a tabela de carros
CREATE TABLE carros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    modelo VARCHAR(100) NOT NULL,
    marca VARCHAR(100) NOT NULL,
    potencia INT NOT NULL,       -- potência em cavalos (hp)
    ano INT NOT NULL,
    carroceria VARCHAR(50) NOT NULL
);

-- Inserindo alguns carros de exemplo para podermos jogar
INSERT INTO carros (modelo, marca, potencia, ano, carroceria) VALUES
('Civic', 'Honda', 155, 2020, 'Sedan'),
('Corolla', 'Toyota', 144, 2019, 'Sedan'),
('Mustang', 'Ford', 450, 2021, 'Cupê'),
('Uno Mille', 'Fiat', 70, 2010, 'Hatch'),
('Gol', 'Volkswagen', 105, 2018, 'Hatch'),
('Onix', 'Chevrolet', 116, 2022, 'Hatch'),
('Ranger', 'Ford', 200, 2021, 'Picape'),
('Hilux', 'Toyota', 204, 2020, 'Picape'),
('Compass', 'Jeep', 178, 2021, 'SUV'),
('Renegade', 'Jeep', 139, 2019, 'SUV'),
('320i', 'BMW', 184, 2022, 'Sedan'),
('A3', 'Audi', 190, 2021, 'Hatch'),
('Celta', 'Chevrolet', 78, 2012, 'Hatch'),
('Sandero', 'Renault', 118, 2019, 'Hatch'),
('T-Cross', 'Volkswagen', 150, 2020, 'SUV'),
('Argo', 'Fiat', 109, 2022, 'Hatch'),
('Cronos', 'Fiat', 130, 2023, 'Sedan'),
('Polo', 'Volkswagen', 128, 2022, 'Hatch'),
('Fox', 'Volkswagen', 104, 2021, 'Hatch'),
('Kwid', 'Renault', 70, 2023, 'Hatch'),
('Creta', 'Hyundai', 166, 2022, 'SUV'),
('HR-V', 'Honda', 173, 2023, 'SUV'),
('Corvette Stingray', 'Chevrolet', 495, 2021, 'Coupé'),
('Astra', 'Chevrolet', 140, 2011, 'Hatch'),
('Palio', 'Fiat', 85, 2017, 'Hatch');

