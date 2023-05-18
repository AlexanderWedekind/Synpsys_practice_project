import random
from typing import Literal


dictionary = ["able", "brunch", "clear", "drive"]

pastGuesses = ""

guessedLetter = ""

displayWord = ""

lives = 12

def resetLives():
    lives = 12
    return lives

def chooseAWord(dictionary):
    chosenword = random.choice(dictionary)
    return chosenword

def makeDisplayWord(chosenWord):
    displayWord = ""
    for each in chosenWord:   
        aSpace = "_"
        displayWord = displayWord + aSpace
    
    return displayWord



def receiveGuessFromPlayer():
    print('Make another guess!\n(press any key, then hit ENTER):')
    guessedLetter = input()
    return guessedLetter 

def rememberGuess(guessedLetter):
    pastGuesses = pastGuesses + guessedLetter
    return pastGuesses

def play(lives, displayWord, pastGuesses):
    print(f"you have {lives} lives left.\nyour word so far: {displayWord}\nletters used so far: {pastGuesses}")
    nextGuess = input("guess a letter:\n(any key + ENTER)")
    lives = lives + 1
    return nextGuess

def checkNextGuess(nextGuess):
    for letter in chosenWord:
        if letter == nextGuess:
            displayWord[chosenWord.index(nextGuess)]

def askToPlay():
    answer = input("Do you want to play hangman?\nchoose (y)es, or (n)o, then press ENTER")
    if answer == "y":
       play()
    
play()


chosenWord = chooseAWord(dictionary)

print(chosenWord)

print(makeDisplayWord(chosenWord))

guessedLetter = receiveGuessFromPlayer()

print(f"Your guess: {guessedLetter}")