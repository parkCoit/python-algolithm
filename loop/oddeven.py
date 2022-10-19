from randomlist import Randomlist # randomlist 파일 안에있는 Class 를 가져온다

class OddEven(object):
    def __init__(self) -> None:
        pass

    def print(self): 
        print( Randomlist().get_random(1,100,10) )  # 가져온 Class 안에있는 get_random()값 입력
        for i in Randomlist().get_random(1,100,10):   # 리스트 안에있는걸 열어본다
            if i % 2 == 0 :
                print(f"짝수 : {i}" )
            else:
                print(f"홀수 : {i}")

    @staticmethod
    def main():
        oddeven = OddEven()
        oddeven.print()

OddEven.main()