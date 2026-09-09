CREATE DATABASE customer;
USE customer;

CREATE TABLE purchase(
trans_id INT PRIMARY KEY,
cust_id INT,
purs_date DATE
);

INSERT INTO purchase
VALUES
(301, 1, "2024-01-10"),
(302, 2, "2024-01-12"),
(303, 1, "2024-02-15"),
(304, 2, "2024-02-20"),
(305, 1, "2024-03-05");

SELECT cust_id ,
MIN(purs_date) AS first_purchase,
MAX(purs_date) AS last_purchase
FROM purchase
GROUP BY cust_id;