import tel_book_func as tb

tb.create_table()
tb.create_table2()
while True:

    menu = input('''
    이번호 누구 번호??

    1. 전화번호 등록   2. 전화번호 찾기  3. 전화번호 수정   4. 전화번호 삭제  5. 종료
    >>> 
    ''')

    if menu == '1':
        login = input('''
        로그인이 필요한 서비스입니다. 로그인 하시겠습니까?
        1. 로그인   2. 회원가입   3. 종료
        >>> 
        ''')
        if login == '1':
            tb.login_telBook()
        elif login == '2':
            tb.sign_in()
            tb.insert_telBook()
        elif login == '3':
            break
        else:
            break
    elif menu == '2':
        tb.search_telBook()
    elif menu == '3':
        tb.update_telBook()
    elif menu == '4':
        pass
    elif menu == '5':
        break
    else :
        print('아직 등록되지 않은 번호입니다. 등록하시겠습니까?')