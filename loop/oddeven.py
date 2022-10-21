from randomlist import Randomlist # randomlist 파일 안에있는 Class 를 가져온다

class OddEven(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def print():
        rl = Randomlist().get_random(1,100,10)
        print(rl)# 가져온 Class 안에 있는 get_random()값 입력
        for i in rl:   # 리스트 안에 있는걸 열어 본다
            if i % 2 == 0 :
                print(f"짝수 : {i}" )
            else:
                print(f"홀수 : {i}")

        print([ f"짝수 : {i}" if i % 2 == 0 else f"홀수 : {i}" for i in rl])
        [i if True else i for i in []]



    @staticmethod
    def main():
        oddeven = OddEven()
        oddeven.print()

OddEven.main()