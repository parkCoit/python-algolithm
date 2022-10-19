from random import random

import random

from scipy.misc import derivative

class Bubblesort(object):
    def __init__(self) -> None:
        pass

    def extrac_random(self):
        self.random = random.sample(range(1,100), 10)

    def sortArray(self):
        for i in self.random :
            if i % 2 == 0:
                print(f"짝수 : {i}" )
            else : print(f"홀수 : {i}")

    def print_bubblesort(self):
        print(self.sortArray())

    @staticmethod
    def main():
        bubblesort = Bubblesort()
        bubblesort.extrac_random()
        bubblesort.print_bubblesort()

Bubblesort.main()     