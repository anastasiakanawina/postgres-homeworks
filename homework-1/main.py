"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="password"
)


EMPLOYEES = [
    (1, "Petr Petrov", "manager", 40000),
    (2, "Maria Ivanova", "sales", 80000),
    (3, "Oleg Kuznetzov", "sales", 50000),
    (4, "Sergei Sergeev", "sales", 90000),
    (5, "Petr Ivanov", "manager", 70000)
]

CUSTOMERS = [
    (11, 33, "Ivan", 89133456733),
    (12, 42, "Anastasia", 89352618490),
    (13, 18, "Mikhail", 89064537895),
    (14, 26, "Andrey", 89678038902)
]

ORDERS = [
    (111, "televizor", 20790, 4, 14),
    (112, "telefon", 34905, 4, 13),
    (113, "holodilnik", 52049, 1, 11),
    (114, "microvawe", 2309, 5, 12),
    (115, "telephone", 59867, 2, 14)
]

cur = conn.cursor()

with conn:
    with conn.cursor() as cur:
        cur.executemany("""
                    INSERT INTO employees VALUES
                     (%s, %s, %s, %s);
                """, EMPLOYEES)
        conn.commit()

    with conn.cursor() as cur:
        cur.executemany("""
                    INSERT INTO customers VALUES
                     (%s, %s, %s, %s);
                """, CUSTOMERS)
        conn.commit()

    with conn.cursor() as cur:
        cur.executemany("""
                    INSERT INTO orders VALUES
                     (%s, %s, %s, %s, %s);
                """, ORDERS)
        conn.commit()

