"""
이름 , 전회번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 개발하시오.
단, 인명은 여러명 저장 가능합니다.
"""


from typing_extensions import Self


class Contact(object):
    def __init__(self, name , num, mail, adr) -> None:
        self.name = name
        self.num = num
        self.mail = mail
        self.adr = adr

    def print_info(self):
        print(f" {self.name}, {self.num}, {self.mail}, {self.adr} ")
        
    @staticmethod 
    def new_contact():  # 인스턴스 new 새로만든다 이런느낌
        name = input(" 이름 : ")        # 1회만 사용
        num = input( "전화 번호 : ")
        mail = input(" 이메일 : ")
        adr = input(" 주소 : ")
        return Contact(name, num, mail, adr) # 생성자



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
        [i.print_info() for i in ls] # for i in ls : i.print_info() 와 같다


    @staticmethod
    def delete_contact(ls, name):
        del ls[[ i for i, j in enumerate(ls)  if  j.name == name  ][0]]





    @staticmethod
    def main():
        ls = []
        while True:
            menu = Contact.print_menu()
            if menu == 1:
                print(" ### 연락처 등록 ###")
                contact = Contact.new_contact() # contact는 instence Contact 는 class
                ls.append(contact) # append(첨부 하다)는 ls 안에 contact를 첨부 한다는 뜻
            elif menu == 2:
                print(" ### 연락처 목록 ###")
                Contact.print_contacts(ls) # 복수형 이라 contacts 로 사용함 한번에 출력 하니(이건 디테일 습관으로...)
            elif menu == 3:
                print(" ### 연락처 삭제 ###")
                Contact.delete_contact(ls, input(" 이름: "))
            elif menu == 4:
                print(" 주소록 어플을 종료 합니다 ")
                break
            else : print("잘못된 값")

Contact.main()