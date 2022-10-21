
import random



class Bubblesort(object):
    def __init__(self) -> None:
        pass

    def extrac_random(self):
        return random.sample(range(1,100), 10)

    def sortArray(self):
        random = self.extrac_random()
        [print(i) for i in random.index()]
           

    def print_bubblesort(self):
        print(self.sortArray())

    @staticmethod
    def main():
        bubblesort = Bubblesort()
        bubblesort.print_bubblesort()

Bubblesort.main()     