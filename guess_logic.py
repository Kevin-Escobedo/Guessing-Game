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
        if not self.guessed_number:
            self.tries += 1
            if guess > self.number:
                return "Lower"
            elif guess < self.number:
                return "Higher"
            else:
                self.guessed_number = True
                return "Correct"
            
    def auto_guess(self):
        '''Tries to guess the number using binary search'''
        lower = 0
        upper = 100
        while not self.guessed_number:
            guess = int((upper + lower) * 0.5)
            result = self.check_guess(guess)
            if result == "Lower":
                upper = guess
            elif result == "Higher":
                lower = guess
        return self.tries


if __name__ == "__main__":
    g = GuessingGame()
