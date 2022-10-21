
class Test(object):
    def __init__(self, id, pw, name):
        self.id = id
        self.pw = pw
        self.name = name

    def print_member(self):
        print(f" {self.id} {self.name} {self.name} ")

    @staticmethod
    def print_menu():
        print("1. 회원 가입")
        print("2. 목록 ")
        print("3. 삭제 ")
        print("4. 종료 ")
        return int(input(" 선택 : "))
    @staticmethod
    def new_member():
        id = input(" 아이디 : ")
        pw = input(" 비밀번호 : ")
        name = input(" 이름 : ")
        return Test(id, pw, name)

    @staticmethod
    def get_member(ls):
        [i.print_member() for i in ls] # for i in ls : i.print_member() 과 같음

    @staticmethod
    def delete_member():
        pass

    @staticmethod
    def main():
        ls = []
        while True :
            menu = Test.print_menu()
            if menu == 1:
                print("### 회원 가입 ###")
                ls.append(Test.new_member())
            elif menu == 2:
                print("### 목록 ###")
                Test.get_member(ls)
            elif menu == 3:
                print("### 삭제 ###")
                Test.delete_member()
            elif menu == 4:
                print("### 종료 ###")
                break
            else : print("잘못 된 값")


Test.main()