import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words)
    print(word)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user has guess
    print(word_letters)

    # getting user input
    while len(word_letters) > 0:
        # letters used
        # ' ' .join['a', 'b', 'cd'] ---> 'a b cd"
        print('You have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
       
        word_list = ["a"  if 'e' in used_letters  else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        #user_letter - is user input letter
        #alphabet - is the entire Alphabet 
        #used_letters - Letters we have already used
        #word_letters - letters for word
        #word_list - Dashes
        if user_letter in alphabet - used_letters:
          
            used_letters.add(user_letter)


           

            if user_letter.lower() in word_letters:
                print('testing debug')
                word_letters.remove(user_letter.lower())
                print(word_letters)

        elif user_letter in used_letters:
            print('You already guessed this letter. Please try again.')

        else:
            print('Invalid character. Please try again.')
        
    # gets here when len(word_letters) == 0


hangman()