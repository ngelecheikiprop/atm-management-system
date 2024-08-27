-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS atm_db;
CREATE USER IF NOT EXISTS 'atmadmin'@'localhost' IDENTIFIED BY 'iamtheadmin';
GRANT ALL PRIVILEGES ON `atm_db`.* TO 'atmadmin'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'atmadmin'@'localhost';
FLUSH PRIVILEGES;
