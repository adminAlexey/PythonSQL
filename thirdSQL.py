import sqlite3
connection = sqlite3.connect("third.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS transfers (
"from" INTEGER NOT NULL,
"to" INTEGER NOT NULL,
amount INTEGER NOT NULL,
tdate TEXT NOT NULL
)
''')

cursor.execute("DELETE FROM transfers")

cursor.execute("INSERT INTO transfers (`from`, `to`, amount, tdate) VALUES (1, 2, 500, date('2023-02-23'))")
cursor.execute("INSERT INTO transfers (`from`, `to`, amount, tdate) VALUES (2, 3, 300, date('2023-03-01'))")
cursor.execute("INSERT INTO transfers (`from`, `to`, amount, tdate) VALUES (3, 1, 200, date('2023-03-05'))")
cursor.execute("INSERT INTO transfers (`from`, `to`, amount, tdate) VALUES (1, 3, 400, date('2023-04-05'))")
cursor.execute("INSERT INTO transfers (`from`, `to`, amount, tdate) VALUES (5, 4, 700, date('2023-01-05'))")

cursor.execute('''
CREATE TABLE IF NOT EXISTS result (
acc INTEGER NOT NULL,
dt_from DATA NOT NULL,
dt_to DATA NOT NULL,
balance INTEGER NOT NULL
)
''')

cursor.execute("DELETE FROM result")

############################################################
transfers = []
for row in cursor.execute('SELECT * FROM transfers ORDER BY tdate'):
    transfers.append(row)
    print(row)

set_account = set()
for row in cursor.execute('SELECT `from` FROM transfers UNION SELECT `to` FROM transfers'):
    set_account.add(row[0])


for s in set_account:
    amount = 0
    last_date = ""
    for t in range(len(transfers)):
        if transfers[t][0] == s:
            amount -= transfers[t][2]
            cursor.execute("INSERT INTO result (acc, dt_from, dt_to, balance) VALUES (?,?,?,?)", (s, transfers[t][3], transfers[t][3], amount))
        elif transfers[t][1] == s: 
            amount += transfers[t][2]
            cursor.execute("INSERT INTO result (acc, dt_from, dt_to, balance) VALUES (?,?,?,?)", (s, transfers[t][3], transfers[t][3], amount))

############################################################

connection.commit()
connection.close()