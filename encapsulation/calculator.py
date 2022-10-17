class Calaulator(object): # object 주는 방식이 상속 Calculator 는 객체
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.num2 = num2
        self.op = op

    def execute(self):  # self는 객체 자신
        num1 = self.num1   # 가독형
        op = self.op
        num2 = self.num2
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        elif op == "%":
            result = num1 % num2
        else:result = "잘못된 연산자 입니다."
        print(f" {num1} {op} {num2} = {result} ")        

if __name__=="__main__":
    num1 = int(input("숫자 :"))
    op = input("연산자 :")
    num2 = int(input("숫자 : "))
    calculator = Calaulator(num1, op, num2)
    calculator.execute()  # 인스턴스 객체