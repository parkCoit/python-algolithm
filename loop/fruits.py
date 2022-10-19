"""
과일판매상에서 메뉴를 진열하는 어플을 제작하고자 한다.
입력되는 값은 없다.
다만, 실행했을 때 출력되는 결과는 다음과 같다.
### 과일번호표 ###
********************************
1번과일: 바나나
2번과일: 사과
3번과일: 망고
********************************
구매할 과일: 바
바나나
"""
class Fruits(object):

    def __init__(self, name) -> None:
        self.menu = ["바나나", "사과", "망고"]
        self.name = name 

    def get_answer(self) :
        name = self.name
        menu = self.menu
        if name == menu[0][:1] or name == menu[0][:2] or name == menu[0][:3]:
            answer = menu[0]
        elif name == menu[1][:1] or name == menu[1][:2] :
            answer = menu[1]
        elif name == menu[2][:1] or name == menu[2][:2] :
            answer = menu[2]
        else : answer = "잘못된 값"

        return answer


    def print_menu(self):
        print("### 과일번호표 ###")
        num = 1
        for i in self.menu:
            print(f"{num}번 과일 : {i}")
            num += 1
        print("********************************")
        print(f"구매한 과일 : {self.name} \n {self.get_answer()} ")
        print("********************************")
    
    @staticmethod
    def main():
        name = input("과일 이름: ")
        fruits = Fruits(name)
        fruits.print_menu()

Fruits.main()