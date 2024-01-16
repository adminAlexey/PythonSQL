# Требуется составить расписание случайных проверок.
# Создайте оператор выбора, который выдаст 100 дат, 
# начиная с текущей, при этом каждая дата отличается 
# от предыдущей на 2-7 дней.
# Пример: 
# 25.02.2023
# 28.02.2023
# 04.03.2023
# 06.03.2023
# 13.03.2023
# 16.03.2023

import sqlite3

connection = sqlite3.connect("second.db")
cursor = connection.cursor()

cursor.execute('''WITH RECURSIVE
checking (curr, next)
AS
( SELECT date(),  date('now','+'||(abs(random() % 6) + 2)||' days')
UNION ALL
SELECT  next, date(next,'+'||(abs(random() % 6) + 2)||' days') FROM checking 
LIMIT 100 ) 
SELECT curr FROM checking
''')

connection.commit()
connection.close()