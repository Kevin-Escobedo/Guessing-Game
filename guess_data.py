#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
from guess_logic import GuessingGame

if __name__ == "__main__":
    data = dict()
    for i in range(101):
        game = GuessingGame()
        game.number = i
        data.update({i:game.auto_guess()})

    file = open("guess_data.txt", "w")

    for key in data:
        file.write("{}: {}\n".format(key, data[key]))
    file.flush()
    file.close()
        
    
