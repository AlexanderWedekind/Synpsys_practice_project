import random
from typing import Literal

dictionary = ["able", "brunch", "clear", "drive"]

def chooseAWord(dictionary):
    chosenword = random.choice(dictionary)
    return chosenword

chosenWord = chooseAWord(dictionary)

print(chosenWord)

def makeDisplayWord(chosenWord):
    displayWord = ""
    for each in chosenWord:   
        aSpace = "_"
        displayWord = displayWord + aSpace
    
    return displayWord

print(makeDisplayWord(chosenWord))

def receiveGuessFromPlayer():
    print('Make another guess!\n(press any key, then hit ENTER):')
    guessedLetter = input()
    return guessedLetter 

guessedLetter = receiveGuessFromPlayer()

print(f"Your guess: {guessedLetter}")