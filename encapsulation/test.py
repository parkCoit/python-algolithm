"""
이름, 주민번호 (950101-1), 주소를 입력받아서 
회원명부를 관리하는 어플을 제작하고자 한다.
출력되는 결과는 다음과 같다.
### 자기소개어플 ###
********************************
이름: 홍길동
나이: 25세 (만나이)
성별: 남성
주소: 서울
********************************
"""

class Test(object):
    def __init__(self, name , num , adr):
        self.name = name
        self.num = num
        self.adr = adr

    def set_age(self):
        num = self.num
        gender_cheaker = num[-1]
        

    def print_person(self):
        title = "### 자기소개어플 ###"
        arster = "*"*30
        print(f" {title} \n {arster} \n 이름 : {self.name} \n 나이 :   \n 성별 :   \n  주소 : {self.adr} ")

    def main():
        name = input("이름 :")
        num = input(" 주민번호 : ")
        adr = input( "주소 :" )
        test = Test(name , num , adr)
        test.print_person()

Test.main()
