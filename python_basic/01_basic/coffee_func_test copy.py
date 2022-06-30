# # 커피자판기
# 1. 커피자판기 2. 메뉴추가 3.메뉴삭제 4.메뉴목록 5.종료
# - 프로그램이 시작될때 필요한 정보를 읽어서 시작합니다.
# - 커피자판기 무한반복하면서 돈을 입력받고, 메뉴를 선택해서 처리
# - 메뉴추가 자판기에서 판매하는 메뉴를 추가하는 기능(메뉴명,가격)
# - 메뉴삭제는 전체 목록을 보여주고 삭제하고자하는 항목을 선택하도록 해서 삭제 처리
# - 메뉴목록은 메뉴이름순,메뉴가격순으로 정렬해서 보여줌.
# - 종료는 메뉴 정보를 저장하고 종료합니다.
import sys

class Coffee:
    def data_load(self):
        f = open(self.path, 'r')
        data = json.load(f)
        f.close()
        return data

    def data_save(self, data):
        f = open(self.path,'w')
        json.dump(data,f)
        f.close()

    item = self.data_load('python_basic\01_basic\item.json')
    def menu_display():
        menu_display = '''
        --------------------------------------------------------
        1.커피자판기   2.메뉴추가  3.메뉴삭제  4.메뉴목록  5.종료
        --------------------------------------------------------
        >>> '''
        menu = input(menu_display)
        return menu

    
    def exe(self, menu):
        if menu == '1':
            self.coffee_m()
                
        elif menu =='2':
            self.menu_add()

        elif menu == '3':
            self.menu_del()

        elif menu =='4':
            self.menu_list()

        elif menu == '5':
            self.data_save('python_basic\01_basic\self.item.json', self.item)
            sys.exit()
        else:
            print('메뉴를 잘못 선택하셨습니다.')

    def __init__(self):
        self.item = self.data_load('python_basic\01_basic\item.json')
        while True:
            self.exe(self.menu_display())
    
    Coffee()