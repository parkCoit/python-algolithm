class Calculator(object): # class 상수, (object) = 상속 → Calculator가 객체가 됨 sava 된 객체
    def __init__(self, num1, op, num2): # 생성자(객체 생성자) 캡슐화
        self.num1 = num1    # 속성 프로퍼티 logic(a = 3 이런식)
        self.op = op
        self.num2 = num2    # 속성
        
    def cal(self): # def Method, self 객체 자신을 의미
        num1 = self.num1
        op = self.op
        num2 = self.num2
        if self.op == "+":
            result = num1 + num2
        elif self.op == "-":
            result = num1 - num2
        elif self.op == "*":
            result = num1 * num2
        elif self.op == "/":
            result = num1 / num2
        elif self.op == "%":
            result = num1 % num2
        else :
            result = "잘못된 연산자 입니다."
        print(f"{num1} {op} {num2}  = {result}")

    @staticmethod # @ 는 장식자다 데코러이터  wrapping
    def main():    # self 값 주지않음 static 
        num1 = int(input("숫자 : "))
        op = input("연산자 : ")
        num2 = int(input("숫자 : "))
        calculator = Calculator(num1, op, num2) # Calculator의 인스턴스화(메모리로 이동) loding 된 객체 은닉화 위 코드 몰라얜 , Calculator(num1, op, num2) -> 생성자(constructor) 인스턴스를 만듬
        calculator.cal() # Calculator = 인스턴스 객체

Calculator.main()