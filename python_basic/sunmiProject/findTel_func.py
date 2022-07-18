import sqlite3

#-------create table----------------------------------------------------
def creat_table():
    conn = sqlite3.connect('python_basic/sunmiProject/tel_find.db')
    cur = conn.cursor()
    cur.execute('''
    create table if not exists telBooks(
        tel text,
        tel_name text,
        info text,
        user_id text
    )
    ''')
    conn.commit()
    conn.close()

def create_table2():
    conn = sqlite3.connect('python_basic/sunmiProject/tel_find.db')
    cur = conn.cursor()
    cur.execute('''
    create table if not exists users(
        user_ID text,
        user_name text,
        user_pass text
    )
    ''')
    conn.commit()
    conn.close()

#-------create table----------------------------------------------------

def insert_telNumber():
    conn = sqlite3.connect('python_basic/sunmiProject/tel_find.db')
    cur = conn.cursor()
    tel = input('등록할 전화번호를 입력하세요 >>>')
    name = input('등록할 전화번호의 이름을 입력하세요 >>>')
    info = input('등록할 전화번호의 정보를 입력하세요 >>>')
    user_id = input('본인 아이디를 입력하세요 >>>')
    sql = f'insert into telBooks values(?, ?, ?, ?)'
    data = (tel, name, info, user_id)
    cur.execute(sql, data)
    conn.commit()
    print('**********************\n 등록이 완료되었습니다~👏 \n**********************')
    conn.close()

def search_telNumber():
    conn = sqlite3.connect('python_basic/sunmiProject/tel_find.db')
    cur1 = conn.cursor()
    cur2 = conn.cursor()
    cur3 = conn.cursor()
    tel = input('검색할 전화번호를 입력하세요 >>>')
    cur1.execute(f'select * from telBooks where tel = ?', (tel, )) #없는 번호일 때
    data1 = cur1.fetchone()
    cur2.execute(f'select * from telBooks where tel = ?', (tel, )) #있는 번호일 때
    data2 = cur2.fetchall()
    cur3.execute(f'select * from telBooks where tel like ?', ('%' + tel + '%', ))
    allnumber = cur3.fetchall()
    if data1 is None:
        print('**********************\n 없는 전화번호입니다 \n**********************')
        print('\n검색한 번호와 비슷한 번호입니다.\n')
        for i in allnumber:
            print(f'전화번호: {i[0]} 이름: {i[1]} 상세설명: {i[2]} 작성자: {i[3]}')
    else:
        for item in data2:
            print('==================================================================')
            print(f'\n검색하신 {tel}은 \n이름 : {item[1]} \n상세설명 : {item[2]}입니다.')
            print('==================================================================')
            conn.close()

def update_telNumber():
    conn = sqlite3.connect('python_basic/sunmiProject/tel_find.db')
    cur = conn.cursor()
    tel = input('수정할 전화번호를 입력하세요 >>>')
    passWord = input('패스워드를 입력하세요 >>>')
    cur.execute('select * from users t1, telBooks t2 where t1.user_id = t2.user_id and t2.tel = ? and t1.user_pass = ?', (tel, passWord))
    data = cur.fetchone()
    if data is None:
        print('*********************\n 고칠 대상이 없습니다 \n*********************')
    else:
        col = input('수정할 항목을 고르세요 (tel, name, info) >>>')
        value = input('수정할 내용을 입력하세요 >>>')
        cur.execute(f'update telBooks set {col} = ? where tel = ?', (value, tel))
        print('\n 🎉수정이 완료되었습니다🎉 \n')
        conn.commit()
        conn.close()
    
def delete_telNumber():
    conn = sqlite3.connect('python_basic/sunmiProject/tel_find.db')
    cur = conn.cursor()
    tel = input('삭제할 전화번호를 입력하세요 >>>')
    passWord = input('패스워드를 입력하세요 >>>')
    cur.execute('select * from users t1, telBooks t2 where t1.user_id = t2.user_id and t2.tel = ? and t1.user_pass = ?', (tel, passWord))
    data = cur.fetchone()
    if data is None:
        print('*********************\n 삭제할 대상이 없습니다 \n*********************')
    else:
        cur.execute(f'delete from telBooks where tel = ?', (tel, ))
        print('\n 🎉삭제가 완료되었습니다🎉 \n')
        conn.commit()
        conn.close()

#----------회원---------------------------------------------------------------------

def signin_user():
    conn = sqlite3.connect('python_basic/sunmiProject/tel_find.db')
    cur = conn.cursor()
    user_id = input('사용할 아이디를 입력하세요')
    user_pw = input('패스워드를 입력하세요 (해당 패스워드는 게시물 로그인, 수정, 삭제시 사용됩니다.) >>>')
    user_name = input('사용자 이름을 입력하세요 >>>')
    data = (user_id, user_pw, user_name)
    cur.execute('insert into users values(?, ?, ?)', data)
    conn.commit()
    print('***********************************\n 🎉회원가입이 완료되었습니다~!🎉 \n***********************************')
    conn.close()

def login_user():
    conn = sqlite3.connect('python_basic/sunmiProject/tel_find.db')
    cur = conn.cursor()
    user_id = input('아이디를 입력하세요 >>>')
    user_pw = input('패스워드를 입력하세요 >>>')
    cur.execute('select * from users where user_id = ? and user_pass = ?', (user_id, user_pw))
    data = cur.fetchone()
    if data is None:
        cho = input('''
            '로그인 실패. 회원가입을 하시겠습니까?[1] or 다시 로그인 하시겠습니까?[2]'
        >>>''') 
        if cho == '1':
            signin_user()
        elif cho == '2':
            login_user()
    else:
        print('로그인 성공~!')
        insert_telNumber()
    conn.close()

