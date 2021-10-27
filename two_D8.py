from random import randint

class TwoD8:

    def __init__(self, num_sides=8):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)

