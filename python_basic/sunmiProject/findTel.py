
import findTel_func as ft

ft.creat_table()
ft.create_table2()

while True:
    menu = input('''
    혹시 이번호 아는 사람 있나요?????
    ====================================================================================================
    1. 전화번호 검색       2. 전화번호 등록     3. 전화번호 수정     4. 전화번호 삭제     5. 종료
    ====================================================================================================
    >>>''')
    
    

    if menu == '1':
            ft.search_telNumber()
    elif menu == '2':
        login_user = input('''
        로그인이 필요한 서비스입니다.
        =============================
        1. 로그인      2. 회원가입     
        =============================
        >>>''')
        if login_user == '1':
            ft.login_user()
        elif login_user == '2':
            ft.signin_user()
    elif menu == '3':
        ft.update_telNumber()
    elif menu == '4':
        ft.delete_telNumber()
    elif menu == '5':
        break
    else:
        print('번호를 잘못 입력하셨습니다.')