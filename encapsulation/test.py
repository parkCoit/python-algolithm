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
    def __init__(self, name , ssn, adr) -> None:
        self.name = name
        self.ssn = ssn
        self.adr = adr

    def set_age(self):
        ssn = self.ssn
        

    def print_test(self):
        print(f"이름: {self.name} 나이: 25세 (만나이) 성별: 남성 주소: {self.adr}")

    def main():
        name = input("이름 :")
        ssn = input("주민 번호 :")
        adr = input("주소 :")
        test = Test(name, ssn, adr)
        test.print_test()

Test.main()