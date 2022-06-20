#!/user/bin/env python3
# hangman game
# This game has an english word list

import random
from english_words import words
import string

# check list for valid word
def get_valid_word(words):
    word = random.choice(words) # get list & pick word
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in word
    abc = set(string.ascii_uppercase) # uppercase letters
    used_letters = set() # users guessed

    player_lives = 12
    # gets user input using while loop check there are letter
    while len(word_letters) > 0 and player_lives > 0:
        # used letters
        #  ' '.join (['a','b'...])--> a, b, c...
        print('You have ', player_lives, 'live left. Used letters:', ' '.join(used_letters))

        # word with _missing letter
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Current word: ', ' '.join(word_list))

        #user input
        user_letter = input("Guess a letter: ").upper()

        # check if used add to used list
        if user_letter in abc - used_letters:
            used_letters.add(user_letter)

            # letter in word remove from word letters
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                player_lives -=1
                print(f"Your letter {user_letter} isn't in word")
        # already used
        elif user_letter in used_letters:
            print(f"You have already used {user_letter}, try again. ")

        else:
            print("Invalid character. Try again please.")
    if player_lives == 0:
        print('You so dead...The word was', word)
    else:
        print(f'You got! {word} was right')




# user input
hangman()