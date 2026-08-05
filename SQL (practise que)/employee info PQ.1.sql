CREATE DATABASE xyz_company;
USE xyz_company;

CREATE TABLE employee(
 id INT PRIMARY KEY,
 name VARCHAR (50),
 salary INT
);

INSERT INTO employee
VALUES
(101, "OM", 20000),
(102, "kumar", 30000),
(103, "ravi", 40000);

SELECT * FROM employee;

