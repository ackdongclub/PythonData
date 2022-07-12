
import sqlite3

def create_table():
    conn = sqlite3.connect('python_basic/sunmiProject/tel_find.db')
    cur = conn.cursor()
    cur.execute('''
    create table if not exists telBooks(
        name text, 
        tel integer,
        info text,
        loginID text

    )
    ''')
    conn.commit()
    conn.close()

def create_table2():
    conn = sqlite3.connect('python_basic/sunmiProject/tel_find.db')
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
    conn = sqlite3.connect('python_basic/sunmiProject/tel_find.db')
    cur = conn.cursor()
    cur1 = conn.cursor()
    tel = input('전화번호를 입력하세요 >>>')
    name = input('이름을 입력하세요 >>>')
    info = input('전화번호의 정보를 입력하세요 >>>')
    loginName = input('작성자 아이디를 입력하세요 >>>')
    chkTel = f'select * from telBooks where tel = ?'
    cur.execute(chkTel, (tel, ))
    if chkTel is None:
        sql = f'insert into telBooks values(?, ?, ?, ?)'
        data = (name, tel, info, loginName)
        cur1.execute(sql, data)
        conn.commit()
        print(f'\n******** [전화번호 : {tel} 이름 : {name} 전화정보 : {info}]로 등록 되었습니다. ********\n')
        conn.close()
    elif chkTel in tel:
        print('\n이미 등록된 번호입니다.\n')

def search_telBook():
    conn = sqlite3.connect('python_basic/sunmiProject/tel_find.db')
    cur1 = conn.cursor()
    cur2 = conn.cursor()
    value = input('검색할 번호를 입력하세요 >>>')
    sql = f'select * from telBooks where tel = ?'
    cur1.execute(sql, (value, ))
    if sql is None:
        print('데이터에 입력되지 않은 번호입니다')
        conn.close()
    else:
        data = cur2.fetchall()
        for item in data:
            print(f'검색하신 {item[1]}는 {item[0]}입니다. \n 작성자{item[3]}')
        conn.close()

def update_telBook():
    conn = sqlite3.connect('python_basic/tel_book/tel_book.db')
    cur = conn.cursor()
    cur1 = conn.cursor()
    loginId = input('작성자 아이디를 입력하세요 >>>')
    removeNum = input('비밀번호를 입력하세요 >>>')
    sql = 'select * from users t1, telBooks t2 where t1.loginID = t2.loginID and t1.loginID = ? and t1.passWord = ?'
    cur.execute(sql, (loginId, removeNum))
    if sql in loginId:
        updateTel = input('삭제할 수정할 전화번호를 입력하세요 >>>')
        col = input('변경할 카테고리를 선택하세요 (name, tel, info) >>>')
        value = input('변경 내용을 입력하세요 >>>')
        sql2 = f'update telBooks set {col} = ? where tel = ?'
        cur1.execute(sql2, (updateTel, value))
        print('\n성공적으로 변경되었습니다\n')
        conn.commit()
        conn.close()
    else:
        print('입력이 틀렸습니다 다시 입력해 주세요')
        update_telBook()






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
    conn = sqlite3.connect('python_basic/tel_book/tel_book.db')
    cur = conn.cursor()
    loginId = input('아이디를 입력해주세요 >>>')
    loginPass = input('비밀번호를 입력하세요 >>>')
    sql = 'select * from users where loginID = ? and passWord = ?'
    cur.execute(sql, (loginId, loginPass))

    if sql is None:
        print('\n로그인 실패😢\n')
        login_telBook()
    else:
        print('\n로그인 성공😆\n')
        insert_telBook()
    conn.close()
    
    