--  creating-table
CREATE TABLE Customers (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    address TEXT,
    phone_number VARCHAR(20)
);

-- inserting dataa
INSERT INTO Customers (id,name, email, address, phone_number)
VALUES (1, 'John Doe', 'john@example.com', '123 Main St', '555-1234')

-- inserting 5 rows
INSERT INTO Customers (id, name, email, address, phone_number)
VALUES
    (6, 'Sarah Lee', 'sarah@example.com', '333 Cherry Ln', '555-3333'),
    (7, 'Michael Brown', 'michael@example.com', '444 Pine St', '555-4444'),
    (8, 'Olivia Davis', 'olivia@example.com', '555 Elm Rd', '555-5555'),
    (9, 'William Johnson', 'william@example.com', '666 Oak Ave', '555-6666'),
    (10, 'Sophia Martinez', 'sophia@example.com', '777 Maple St', '555-7777');

-- retreiving data
SELECT id,name,email,address,phone_number
FROM Customers;

SELECT name, email
FROM Customers;


-- customer with id 3
SELECT id, name, email, address, phone_number
FROM Customers
WHERE id=6;

-- Write a query to fetch all customers whose name starts with 'A'.
SELECT id, name, email, address, phone_number
FROM Customers
WHERE name LIKE "A%"

-- Write a query to fetch all customers, ordered by name in descending order.
SELECT id, name, email, address, phone_number
FROM Customers
ORDER BY name DESC

-- Write a query to update the address of the customer with id 4.

UPDATE Customers
set address = "new address"
WHERE id = 4;


-- Write a query to fetch the top 3 customers when ordered by id in ascending order.
SELECT id, name, email, address, phone_number
FROM Customers
ORDER BY id ASC
LIMIT 3;

-- Write a query to delete the customer with id 2.
DELETE FROM Customers
WHERE id = 2;

-- Write a query to count the number of customers.

SELECT COUNT(*) as Customers_count
FROM Customers


-- Write a query to fetch all customers except the first two when ordered by id in ascending order.
SELECT id, name, email, address, phone_number
FROM Customers
ORDER BY id ASC
LIMIT -1 OFFSET 2;

-- Write a query to fetch all customers whose id is greater than 2 and name starts with 'B'.
SELECT id, name, email, address, phone_number
FROM Customers
WHERE id > 2 AND name LIKE 'S%';

-- Write a query to fetch all customers whose id is less than 3 or name ends with 's'.
SELECT id, name, email, address, phone_number
FROM Customers
WHERE id < 3 OR name LIKE '%s';

-- Write a query to fetch all customers where the phone_number field is not set or is null.
SELECT id, name, email, address, phone_number
FROM Customers
WHERE phone_number IS NULL OR phone_number = '';