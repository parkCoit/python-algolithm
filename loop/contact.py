"""
이름 , 전회번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 개발하시오.
단, 인명은 여러명 저장 가능합니다.
"""


from typing_extensions import Self


class Contact(object):
    def __init__(self, name , pnum, mail, adr) -> None:
        self.name = name
        self.pnum = pnum
        self.mail = mail
        self.adr = adr

    def print_info(self):
        print(f" {self.name}, {self.pnum}, {self.mail}, {self.adr} ")
        
    @staticmethod 
    def new_contact():  # 인스턴스 new 새로만든다 이런느낌
        name = input(" 이름 : ")        # 1회만 사용
        pnum = input( "전화 번호 : ")
        mail = input(" 이메일 : ")
        adr = input(" 주소 : ")
        return Contact(name, pnum, mail, adr) # 생성자



    @staticmethod
    def print_menu():
        print("1. 연락처 등록")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 종료")
        menu = input("메뉴 선택:")
        return int(menu)
    
    @staticmethod
    def print_contacts(ls):
        for i in ls :
            i.print_info()

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Contact.print_menu()
            if menu == 1:
                print(" ### 연락처 등록 ###")
                contact = Contact.new_contact() # contact는 instence Contact 는 class
                ls.append(contact) # append(첨부하다)는 ls 안에 contact 를 첨부한다는 뜻
            elif menu == 2:
                print(" ### 연락처 출력 ###")
                Contact.print_contacts(ls) # 복수형이라 contacts 로 사용함 한번에 출력하니(이건 디테일 습관으로)
            elif menu == 3:
                print(" ### 연락처 삭제 ###")
            elif menu == 4:
                print(" 주소록 어플을 종료합니다 ")

Contact.main()