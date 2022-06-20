#!/user/bin/env python3
# random number game
import random

# define function para x
def guess(x):
    # get rand num
    random_number = random.randint(1, x)
    guess = 0
    # guess number keep looping
    while guess != random_number:
        # cast to int to compare
        guess = int(input(f'Guess a number between 1 and {x}: '))
        # guess hint
        if guess < random_number:
            print('Sorry, guess again. Too low. ')
        elif guess > random_number:
            print('Sorry, guess again. Too high')
        else:
            print('Winner!', guess, random_number)
            print(f'Winner!!! {random_number} was the number.')
            print(random_number)
guess(10)