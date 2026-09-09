CREATE DATABASE salary;
USE salary;

CREATE TABLE employee(
name VARCHAR(50),
salary INT
);

INSERT INTO employee
VALUES
("om", 90000),
("karan", 80000),
("samay", 70000);

SELECT MAX(salary)
FROM employee
WHERE salary <  (SELECT MAX(salary) FROM employee);