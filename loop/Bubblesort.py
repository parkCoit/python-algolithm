from operator import length_hint
from random import random

import random

from scipy.misc import derivative

class Bubblesort(object):
    def __init__(self) -> None:
        pass

    def extrac_random(self):
        return random.sample(range(1,100), 10)

    def sortArray(self):
        random = self.extrac_random()
        for i in random.index():
            print(i)
           

    def print_bubblesort(self):
        print(self.sortArray())

    @staticmethod
    def main():
        bubblesort = Bubblesort()
        bubblesort.print_bubblesort()

Bubblesort.main()     