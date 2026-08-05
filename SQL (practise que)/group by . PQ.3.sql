CREATE DATABASE Orders;
USE Orders;

CREATE TABLE customer(
order_id INT PRIMARY KEY,
customer_id INT,
order_date DATE
);

INSERT INTO customer 
VALUES
(201, 1, "2024-02-15"),
(202, 2, "2024-02-10"),
(203, 1, "2024-02-18"),
(204, 3, "2024-02-20"),
(205, 1, "2024-02-25"),
(206, 2, "2024-02-27"),
(207, 1, "2024-03-02");

SELECT customer_id ,  COUNT(order_id)
AS total_orders
FROM customer
GROUP BY customer_id; 