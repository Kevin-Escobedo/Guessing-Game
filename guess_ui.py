#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
import tkinter
import guess_logic
import os
import sys

class GameInterface:
    def __init__(self):
        self.root_window = tkinter.Tk()
        self.root_window.geometry("300x150")
        self.root_window.title("Guessing Game")
        self.root_window.resizable(0, 0)
        self.root_window.iconbitmap(self.resource_path("question_mark.ico"))
        self.game = guess_logic.GuessingGame()
        self.guess_entry = tkinter.Entry(self.root_window)
        self.result = tkinter.StringVar()
        self.show_tries = tkinter.StringVar()

    def resource_path(self, relative_path):
        '''Get absolute path to resource'''
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def get_guess(self):
        '''Gets the guess from Entry'''
        try:
            guess = int(self.guess_entry.get())
            if guess < 0:
                raise ValueError
            return guess
        except ValueError:
            self.result.set("Invalid guess")

    def check(self):
        '''Checks the guess'''
        guess = self.get_guess()
        self.result.set(self.game.check_guess(guess))


    def run(self):
        '''Runs the GUI'''
        tkinter.Label(self.root_window, text = "Enter Guess").grid(row=0, column=0)
        self.guess_entry.grid(row = 0, column = 1, sticky = tkinter.NSEW)

        tkinter.Label(self.root_window, textvariable = self.show_tries).grid(row = 2, column = 1)
        self.show_tries.set("Tries: {}".format(self.game.tries))

        tkinter.Label(self.root_window, textvariable = self.result).grid(row = 1, column = 1)

        self.root_window.mainloop()

if __name__ == "__main__":
    GameInterface().run()
