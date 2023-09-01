-- Напишите запросы, которые выводят следующую информацию:
-- 1. Название компании заказчика (company_name из табл. customers) и ФИО сотрудника, работающего над заказом этой компании (см таблицу employees),
-- когда и заказчик и сотрудник зарегистрированы в городе London, а доставку заказа ведет компания United Package (company_name в табл shippers)

SELECT c.company_name, CONCAT(e.first_name, ' ', e.last_name) as fio
FROM orders AS o
LEFT JOIN customers AS c ON USING(customer_id)
LEFT JOIN employees AS e ON USING(employee_id)
LEFT JOIN shippers AS s ON o.ship_via=s.shipper_id
WHERE 1=1
	AND c.city = 'London'
	AND e.city = 'London'
	AND s.company_name = 'United Package'

-- 2. Наименование продукта, количество товара (product_name и units_in_stock в табл products),
-- имя поставщика и его телефон (contact_name и phone в табл suppliers) для таких продуктов,
-- которые не сняты с продажи (поле discontinued) и которых меньше 25 и которые в категориях Dairy Products и Condiments.
-- Отсортировать результат по возрастанию количества оставшегося товара.

SELECT p.product_name, p.units_in_stock, s.contact_name, s.phone
FROM products as p
LEFT JOIN categories as c ON USING(category_id)
LEFT JOIN suppliers as s ON USING(supplier_id)
WHERE discontinued != 1 and category_name in ('Dairy Products', 'Condiments')
  		AND units_in_stock < 25
ORDER BY p.units_in_stock

-- 3. Список компаний заказчиков (company_name из табл customers), не сделавших ни одного заказа

SELECT c.company_name
FROM customers AS c
LEFT JOIN orders AS o ON USING(customer_id)
WHERE order_id is null

-- 4. уникальные названия продуктов, которых заказано ровно 10 единиц (количество заказанных единиц см в колонке quantity табл order_details)
-- Этот запрос написать именно с использованием подзапроса.

SELECT DISTINCT product_name
FROM products as pr
WHERE EXISTS (SELECT *
                FROM order_details od
                WHERE quantity=10 AND pr.product_id=od.product_id)