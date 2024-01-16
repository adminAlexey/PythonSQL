# Требуется оценить эффективность продавцов. 
# Создайте запрос, который вернёт количество и 
# сумму продаж для каждого продавца, а также 
# ранжирует продавцов по количеству продаж и по 
# сумме продаж.

import sqlite3

connection = sqlite3.connect("second.db")
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS employee")
cursor.execute("DROP TABLE IF EXISTS sales")

cursor.execute('''
CREATE TABLE employee (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name VARCHAR NOT NULL
)
''')

cursor.execute('''
CREATE TABLE sales (
id INTEGER PRIMARY KEY,
employee_id INTEGER,
price INTEGER NOT NULL, 
FOREIGN KEY(employee_id) REFERENCES employee(id)
)
''')

cursor.execute('''
INSERT INTO employee (name) VALUES 
('Ivan'),
('Stepan'),
('Fedor')
''')

cursor.execute('''
INSERT INTO sales (employee_id, price) VALUES 
((SELECT id FROM employee WHERE name='Fedor'), 2500),
((SELECT id FROM employee WHERE name='Ivan'), 4500),
((SELECT id FROM employee WHERE name='Stepan'), 1700),
((SELECT id FROM employee WHERE name='Stepan'), 900),
((SELECT id FROM employee WHERE name='Fedor'), 3500),
((SELECT id FROM employee WHERE name='Fedor'), 1000)
''')

cursor.execute('''
SELECT 	E.*, 
        (SELECT COUNT(*) 
         FROM sales 
         WHERE E.id = sales.employee_id)
         As sales_c, 
         RANK () OVER (
            ORDER BY
            (SELECT COUNT(*) 
             FROM sales 
             WHERE E.id = sales.employee_id
            ) DESC
          ) AS sales_rank_c,
         (SELECT SUM(price) 
          FROM sales 
          WHERE E.id = sales.employee_id) 
          AS sales_s,
          RANK () OVER (
            ORDER BY
            (SELECT SUM(price) 
             FROM sales 
             WHERE E.id = sales.employee_id
            ) DESC
          ) AS sales_rank_s
FROM employee AS E
''')

connection.commit()
connection.close()