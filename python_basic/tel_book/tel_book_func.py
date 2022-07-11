import sqlite3
from tokenize import String

def create_table():
    conn = sqlite3.connect('python_basic/tel_book/tel_book.db')
    cur = conn.cursor()
    cur.execute('''
    create table if not exists telBooks(
        name text, 
        tel integer,
        info text,
        recommend integer,
        loginID text

    )
    ''')
    conn.commit()
    conn.close()

def create_table2():
    conn = sqlite3.connect('python_basic/tel_book/tel_book.db')
    cur = conn.cursor()
    cur.execute('''
    create table if not exists users(
        loginID text,
        loginName text,
        passWord text
    )
    ''')
    conn.commit()
    conn.close()

#-----------------crud--------------------

def insert_telBook():
    conn = sqlite3.connect('python_basic/tel_book/tel_book.db')
    cur = conn.cursor()
    tel = input('전화번호를 입력하세요 >>>')
    name = input('이름을 입력하세요 >>>')
    info = input('전화번호의 정보를 입력하세요 >>>')
    recommend = 0
    loginName = input('작성자 아이디를 입력하세요 >>>')
    chkTel = f'select tel from telBooks'
    if chkTel is None:
        data = (name, tel, info, recommend, loginName)
        sql = f'insert into telBooks values(?, ?, ?, ?, ?)'
        cur.execute(sql, data)
        print(f'\n******** [전화번호 : {tel} 이름 : {name} 전화정보 : {info}]로 등록 되었습니다. ********\n')
    elif chkTel in tel:
        print('\n이미 등록된 번호입니다.\n')
    conn.commit()
    conn.close()

def search_telBook():
    conn = sqlite3.connect('python_basic/tel_book/tel_book.db')
    cur = conn.cursor()
    value = input('검색할 전화번호를 입력하세요 >>>')
    sql = f'select * from telBooks where tel = ?'
    cur.execute(sql, (value, ))
    data = cur.fetchall()
    for item in data:
        print(f'\n검색하신 {item[1]}는 {item[0]}입니다  \n-{item[4]}-\n')
    conn.commit()
    conn.close()

def update_telBook():
    conn = sqlite3.connect('python_basic/tel_book/tel_book.db')
    cur = conn.cursor()
    loginId = input('작성자 아이디를 입력하세요 >>>')
    removeNum = input('비밀번호를 입력하세요 >>>')
    sql = f'select * from users t1, telBooks t2 where t1.loginID = t2.loginID and t1.passWord = ?'
    cur.execute(sql, (removeNum,))
    if sql is None:
        print('입력이 틀렸습니다 다시 입력해 주세요')
        update_telBook()
    else:
        updateTel = input('삭제할 수정할 전화번호를 입력하세요 >>>')
        col = input('변경할 카테고리를 선택하세요 (name, tel, info) >>>')
        value = input('변경 내용을 입력하세요 >>>')
        sql2 = f'update telBooks set {col} = ? where tel = ?'
        cur.execute(sql2, (updateTel, value))
        print('\n성공적으로 변경되었습니다\n')
    conn.commit()
    conn.close()






#---------로그인 서비스---------
def sign_in():
    conn = sqlite3.connect('python_basic/tel_book/tel_book.db')
    cur = conn.cursor()
    loginID = input('사용하실 아이디를 입력하세요 >>>')
    name = input('이름을 입력하세요 >>>')
    password = input('사용하실 비밀번호를 입력하세요 >>>')
    data = (loginID, name, password)
    sql = 'insert into users values(?, ?, ?)'
    cur.execute(sql, data)
    conn.commit()
    print(f'\n****** [ 회원가입 완료!! {name}님 환영합니다~ ] ****** \n')
    conn.close()

def login_telBook():
    conn = conn = sqlite3.connect('python_basic/tel_book/tel_book.db')
    cur = conn.cursor()
    loginId = input('아이디를 입력해주세요 >>>')
    #loginPass = input('비밀번호를 입력하세요 >>>')
    sql = f'select * from users'
    cur.execute(sql, )
    if sql in loginId:
        print('\n로그인 성공😆\n')
        insert_telBook()
    else:
        print('\n로그인 실패😢\n')
        login_telBook()
    conn.close()
    
    