import sqlite3

test_db = sqlite3.connect("test2.db")

cur = test_db.cursor()

sql = """
create table book(
id int,
name varchar(10),
age int
);
"""

sql2 = """
insert into book values(2,'zjh',22)"""
cur.execute(sql2)
test_db.commit()

sql3 = "select * from book;"
cur.execute(sql3)
data = cur.fetchall()
print(type(data))
print(data)
cur.close()