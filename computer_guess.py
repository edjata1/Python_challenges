#!/user/bin/env python3
# random number game
import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    # if low = high error
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"You got it {guess} was my number.")
computer_guess(10)