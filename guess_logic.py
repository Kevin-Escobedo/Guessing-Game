#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
import random

class GuessingGame:
    def __init__(self):
        self.number = random.randrange(1, 101)
        self.tries = 0
        self.guessed_number = False
    def check_guess(self, guess:int):
        '''Checks how the guess compares to the number'''
        self.tries += 1
        if guess > self.number:
            return "Lower"
        elif guess < self.number:
            return "Higher"
        else:
            return "Correct"
