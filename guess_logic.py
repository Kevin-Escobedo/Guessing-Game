#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
import random

class GuessingGame:
    def __init__(self, lower = 1, upper = 100):
        self.lower = lower
        self.upper = upper
        self.number = random.randrange(self.lower, self.upper + 1)
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
        lower = self.lower - 1
        upper = self.upper + 1
        while not self.guessed_number:
            guess = int((lower + upper) * 0.5)
            result = self.check_guess(guess)
            if result == "Lower":
                upper = guess
            elif result == "Higher":
                lower = guess
        return self.tries


if __name__ == "__main__":
    g = GuessingGame()
