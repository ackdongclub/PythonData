import sqlite3

def create_table():
    conn = sqlite3.connect('python_basic/nameCard/name_Card.db')
    cur = conn.cursor()
    cur.execute( '''
    create table if not exists nameCards(
        idx integer,
        name text,
        tel text,
        fax integer,
        company_name text
    )
    ''')

    conn.commit()
    conn.close()

def insert_nameCard():
    conn = sqlite3.connect('python_basic/nameCard/name_Card.db')
    cur = conn.cursor()
    idx = input('일련번호를 입력하세요 >>>')
    name = input('이름을 입력하세요 >>>')
    tel = input('전화번호를 입력하세요(010-XXXX-XXXX) >>>')
    fax = input('팩스 번호를 입력하세요 >>>')
    company_name = input('회사명을 입력하세요 >>>')
    data = (idx, name, tel, fax, company_name)
    sql = 'insert into nameCards values(?, ?, ?, ?, ?)'
    cur.execute(sql, data)
    conn.commit()
    conn.close()

def list_nameCard():
    conn = sqlite3.connect('python_basic/nameCard/name_Card.db')
    cur = conn.cursor()
    cur.execute('select * from nameCards')
    data = cur.fetchall()
    for item in data:
        print(f'이름:{item[1]} 전화번호:{item[2]} 회사명:{item[4]} fax:{item[3]}')
    conn.close()

def update_nameCard():
    conn = sqlite3.connect('python_basic/nameCard/name_Card.db')
    cur = conn.cursor()
    tel = input('수정할 사람의 연락처를 입력하세요 (010-XXXX-XXXX) >>>')
    col = input('수정할 항목을 선택하세요 (name, tel, fax, company_name) >>>')
    value = input('수정할 내용 >>>')
    sql = f'update nameCards set {col} = ? where tel = ?'
    cur.execute(sql, (value, tel))
    conn.commit()
    conn.close()

def delete_nameCard():
    conn = sqlite3.connect('python_basic/nameCard/name_Card.db')
    cur = conn.cursor()
    value = input('삭제할 사람의 연락처 4자리를 입력하세요 >>>')
    sql = f'delete from nameCards where tel like ?'
    cur.execute(sql, ('%' + value + '%', ))
    conn.commit()
    conn.close()

