import random

def guess(guesedNumber):
    random_number = random.randint(1, guesedNumber)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 anf{guesedNumber}:'))
        if guess < random_number:
            print(f'number too low ')
        elif guess > random_number:
            print('number is too high, try again')

    print(f'you guessed the number {random_number}')

guess(10)