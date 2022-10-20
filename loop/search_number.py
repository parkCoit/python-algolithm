from randomlist import Randomlist 

class SearchNumber(object):
    
    def __init__(self, num) -> None:
        self.num = num

    def print(self):
        rl = Randomlist()
        rl1 = rl.get_random(10 , 100 , 10)
        print(rl1)
        for i in rl1:
            if i %  self.num == 0:
                print(i)

    @staticmethod
    def main():
        num = int(input("배수 : "))
        search_number = SearchNumber(num)
        search_number.print()

SearchNumber.main()