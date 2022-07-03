import cx_Oracle

# print(cx_Oracle)
conn = cx_Oracle.connect('')
cur = conn.cursor()
sql = ''
cur.excute(sql)
data = cur.fetchall()
for item in data:
    print(item)
conn.close()