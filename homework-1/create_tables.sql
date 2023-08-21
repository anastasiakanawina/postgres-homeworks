-- SQL-команды для создания таблиц
CREATE TABLE employees
(
    id serial PRIMARY KEY,
    name varchar(100) NOT NULL,
    job_title text,
	salary int
);


CREATE TABLE customers
(
    id int PRIMARY KEY,
    age int,
    name varchar(100) NOT NULL,
    phone varchar(20) NOT NULL UNIQUE
);


CREATE TABLE orders
(
    id serial PRIMARY KEY,
    name_product text,
	price int,
	employees_id int,
	customer_id int,
	FOREIGN KEY (employees_id)  REFERENCES employees (id),
	FOREIGN KEY (customer_id)  REFERENCES customers (id)
);