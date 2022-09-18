from ast import Num
import numbers
import random
from tokenize import Number

print("Hello, let's play a game. \nYou choose a number, and the computer will tru to guess it.")
input("Press 'enter' when ready")
print("Great!")


def askForResponse(guess):
    response = input(f"Is {guess} your number (y), or is that too high (h), or too low (l)?\n(Press 'y' for yes, 'l' for low, or 'h' for high. then press 'enter')")
    return response

def evaluateAnswers(response, guess, lowerLimit, upperLimit):
    if response == "y":
        computerWon()
    if response == "h":
        computerGuesses(lowerLimit, guess-1)
    if response == "l":
        computerGuesses(guess+1, upperLimit)
    if response != "y":
        print("Please answer with 'y', 'h' or 'l'.")
        evaluateAnswers(askForResponse(guess), guess)

def computerGuesses(lowerLimit, upperLimit):
    guess = random.randint(lowerLimit, upperLimit)
    
    evaluateAnswers(askForResponse(guess), guess, lowerLimit, upperLimit)
    
    
def computerWon():
    print("Computer won!")
    playAgain = askToPlay()
    if playAgain == "y":
        print("Let's go!")
        computerGuesses(1, 1000)
    else:
        print("Thanks for playing, see you next time.")


def askToPlay():
    yesOrNo = input("Hit 'y'and then 'enter' to play again, or any other key + 'enter' to quit")
    return yesOrNo

computerGuesses(1, 1000)