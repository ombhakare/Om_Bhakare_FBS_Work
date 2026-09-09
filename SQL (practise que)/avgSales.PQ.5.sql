CREATE DATABASE orders;
USE orders;

CREATE TABLE sales(
sales_id INT PRIMARY KEY,
region VARCHAR (50),
sales_amount INT
);

INSERT INTO sales
VALUES
(501, "NORTH", 50000),
(502, "SOUTH", 70000),
(503, "NORTH", 80000),
(504, "WEST", 90000);

SELECT region , AVG(sales_amount) 
FROM sales 
GROUP BY region;