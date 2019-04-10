import sqlite3
# 聚合函数create_aggregate(name, num_params, aggregate_class)
# name是实例名， num_params为-1时,类aggregate_class中step函数可以接受无数个参数，num_params指定step函数传的参数
class MySum:
    def __init__(self):
        self.count = 0

    def step(self, value):
        self.count += value

    def finalize(self):
        return self.count

con = sqlite3.connect(":memory:")
con.create_aggregate("mysum", 1, MySum)
cur = con.cursor()
cur.execute("create table test(i)")
cur.execute("insert into test(i) values (1)")
cur.execute("insert into test(i) values (2)")
# cur.execute("select mysum(i) from test")
cur.execute("select * from test")
print(cur.fetchall())
# print(cur.fetchone()[0])