from ast import Num
import numbers
import random
from tokenize import Number

print("Hello, let's play a game. \nYou choose a number, and the computer will tru to guess it.")
input("Press 'enter' when ready")
print("Great!")

playAgain = "y"
lowerLimit = 1
upperLimit = 1000



def computerGuesses(lowerLimit, upperLimit):
    guess = random.randint(lowerLimit, upperLimit)
    response = input(f"Is {guess} your number (y), or is that too high (h), or too low (l)?\n(Press 'y' for yes, 'l' for low, or 'h' for high")
    if response == "y":
        computerWon()
    if response == "h":
        computerGuesses(lowerLimit, upperLimit-1)
    if response == "l":
        computerGuesses(lowerLimit+1, upperLimit)
    else:
        response = input(f"Is {guess} your number (y), or is that too high (h), or too low (l)?\n(Press 'y' for yes, 'l' for low, or 'h' for high")      
    
def computerWon():
    print("Computer won!")
    askToPlay()
    if playAgain == "y":
        print("Let's go!")
        lowerLimit = 1
        upperLimit = 1000
        computerGuesses(lowerLimit, upperLimit)


def askToPlay():
    playAgain = input("Hit 'y' to play again, or any other key to quit")
    return playAgain