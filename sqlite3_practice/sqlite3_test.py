import sqlite3
# conn = sqlite3.connect('example.db')
#
# c = conn.cursor()
#
# c.execute('''create table stocks (date text, trans text, symbol text, qty real, price real)''')
#
# c.execute("insert into stocks values ('2019-03-21', 'BUY', 'RHAT', 100, 35.14)")
#
# conn.commit()
#
# conn.close()

# -----------------
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Never do this -- insecure!
symbol = 'RHAT'
c.execute("SELECT * FROM stocks WHERE symbol = '%s'" % symbol)

# Do this instead
t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)
conn.commit()

conn.close()