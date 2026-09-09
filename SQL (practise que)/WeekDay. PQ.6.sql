CREATE DATABASE seven;
USE seven;

CREATE TABLE weeks(
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE
);

INSERT INTO weeks
VALUES
(405, 1, "2024-02-17"),
(406, 2, "2024-02-18"),
(407, 3, "2024-02-19"),
(408, 1, "2024-02-25");

SELECT * from weeks
WHERE DAYOFWEEK(order_date) IN (1,7);