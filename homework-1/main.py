"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="password"
)

cur = conn.cursor()

cur.execute("""
                INSERT INTO employees VALUES
                (1, 'Petr Petrov', 'sales', 40000),
                (2, 'Maria Ivanova', 'manager', 80000),
                (3, 'Oleg Kuznetzov', 'sales', 50000),
                (4, 'Sergei Sergeev', 'sales', 90000),
                (5, 'Petr Ivanov', 'manager', 70000);
            """)

conn.commit()

cur.execute("""
                INSERT INTO customers VALUES
                (11, 33, 'Ivan', 89133456733),
                (12, 42, 'Anastasia', 89352618490),
                (13, 18, 'Mikhail', 89064537895),
                (14, 26, 'Andrey', 89678038902);
            """)

conn.commit()

cur.execute("""
                INSERT INTO orders VALUES
                (111, 'televizor', 20790, 4, 14),
                (112, 'telefon', 34905, 4, 13),
                (113, 'holodilnik', 52049, 1, 11),
                (114, 'microvawe', 2309, 5, 12),
                (115, 'telephone', 59867, 2, 14);
            """)

conn.commit()
cur.close()
conn.close()
