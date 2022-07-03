import nameCard_func as nc

nc.create_table()
while True:
    menu = input('''
    1. 명함 등록   2. 명함 수정   3. 명함 삭제   4. 리스트 출력   5. 종료
    >>>
    ''')

    if menu == '1':
        nc.insert_nameCard()
    elif menu == '2':
        nc.update_nameCard()
    elif menu == '3':
        nc.delete_nameCard()
    elif menu == '4':
        nc.list_nameCard()
    elif menu == '5':
        break
    else:
        print('잘못 입력하셨습니다')

