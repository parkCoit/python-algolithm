"""
이름 , 전회번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 개발하시오.
단, 인명은 여러명 저장 가능합니다.
"""


class Test(object):


    def __init__(self, name, num, email, addr):
        self.name = name
        self.num = num
        self.email = email
        self.addr = addr

    def print(self):
        pass

    @staticmethod
    def print_menu():
        print("1. 회원 가입 ")
        print("2. 목록")
        print("3. 회원 탈퇴")
        print("4. 종료")
        return int(input("메뉴 선택 :"))

    def print_inf(self):
        print(f"{self.name} {self.num} {self.email} {self.addr} ")

    @staticmethod
    def new_contact():
        name = input("이름 :")
        num = input("전화 번호 :")
        email = input("이메일 :")
        addr = input("주소 :")
        return Test(name, num, email, addr)


    @staticmethod
    def print_contacts(ls):
        for i in ls:
            i.print_inf()

    @staticmethod
    def delete_contact(ls, name):
        for i , j in enumerate(ls):
            if j.name == name :
                del ls[i]

    @staticmethod
    def main():
        ls = []
        while True :
            menu = Test.print_menu()
            if menu == 1 :
                print("### 입력 ### ")
                ls.append(Test.new_contact())
            elif menu == 2 :
                print("### 출력 ### ")
                Test.print_contacts(ls)
            elif menu == 3 :
                print("### 삭제 ### ")
                Test.delete_contact(ls, input("이름 :"))
            elif menu == 4 :
                print("### 종료 ### ")
                break
            else : print(" ### 잘못된 값 ###")



Test.main()