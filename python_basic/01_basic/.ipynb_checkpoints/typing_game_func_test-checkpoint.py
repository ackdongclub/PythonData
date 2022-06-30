# 타자게임
# 데이터 저장 : word = []
# word  리스트에서 문제를 추출하여 제출하면 맞추는 게임
# - 한번 출제된 문제는 맞출때까지 반복
# - 전체 5문제를 출제 다 맞추면 종료

import typing_game_func as tgf
import os

path = os.path.dirname(__file__) #실행하는 파일의 경로 값을 path에 저장
word = tgf.data_load(path + '/word.json') #위도우에서는 \ 사용, 맥에서는 / 사용
rank = tgf.data_load(path + '/rank.json')

menu_display = '''
------------------------------------------------------
1.게임   2.문제추가  3.문제저장 4.등수리스트  5.종료
------------------------------------------------------
>>> '''

while True:
    menu = input(menu_display)
    if menu == '1':
        tgf.game(word,rank)
    elif menu == '2':
        tgf.quiz_add(word)
    elif menu == '3':
        print('문제저장작업')
    elif menu =='4':
        tgf.rank_list(rank)
    elif menu == '5':
        print('프로그램 종료!')
        tgf.data_save(path + '/word.json', word)
        tgf.data_save(path + '/rank.json', rank)
        break
    #elif menu == '6':
        #print(word)
    else:
        print('메뉴를 잘못 선택하셨습니다.')