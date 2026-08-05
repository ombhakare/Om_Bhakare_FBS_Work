CREATE DATABASE company;
USE company;

CREATE TABLE employee (
emp_id INT PRIMARY KEY,
emp_name VARCHAR(50),
emp_salary INT
);

INSERT INTO employee
VALUES
(101, "Alice", 95000),
(102, "Bob", 87000),
(103, "charlie", 91000),
(104, "David", 75000),
(105, "Eve", 99000);


SELECT * 
FROM employee
ORDER BY emp_Salary DESC 
LIMIT 3;