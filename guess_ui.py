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

    def resource_path(self, relative_path):
        '''Get absolute path to resource'''
        base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(base_path, relative_path)

    def run(self):
        '''Runs the GUI'''
        tkinter.Label(self.root_window, text = "Enter Guess").grid(row=0, column=0)
        self.guess_entry.grid(row = 0, column = 1, sticky = tkinter.NSEW)
