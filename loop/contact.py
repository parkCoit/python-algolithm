"""
이름 , 전회번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 개발하시오.
단, 한명은 여러명 저장 가능합니다.
"""


class Contact(object):
    def __init__(self, name , pnum, mail, adr) -> None:
        self.name = name
        self.pnum = pnum
        self.mail = mail
        self.adr = adr

    

    def print(self):
        print(f" {self.name}, {self.pnum}, {self.mail}, {self.adr} ")

    @staticmethod 
    def set_contact():  # 인스턴스
        name = input(" 이름 : ")        # 1회만 사용
        pnum = input( "전화 번호 : ")
        mail = input("이메일 : ")
        adr = input(" 주소 : ")
        return Contact(name, pnum, mail, adr)

    @staticmethod
    def print_menu():
        print("1. 연락처 등록")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 종료")
        menu = input("메뉴 선택:")
        return int(menu)

    @staticmethod
    def main():
        while True:
            menu = Contact.print_menu()
            if menu == 1:
                print(" ### 연락처 등록 ###")
            elif menu == 2:
                print(" ### 연락처 출력 ###")
            elif menu == 3:
                print(" ### 연락처 삭제 ###")
            elif menu == 4:
                print(" 주소록 어플을 종료합니다 ")

Contact.main()