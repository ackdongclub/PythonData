import sqlite3
from symtable import Symbol

conn = sqlite3.connect('python_basic/03_db/example.db')
cur = conn.cursor()

keyword = input('검색어 >>>')
sql = 'select * from stocks where symbol = ?'

cur.execute(sql, (keyword, ))

data = cur.fetchall()
for i in data:
    print(i)

conn.close()