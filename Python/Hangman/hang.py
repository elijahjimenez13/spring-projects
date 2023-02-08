import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word
def hangman():
    #user_letter - is user input letter
    #alphabet - is the entire Alphabet 
    #used_letters - Letters we have already used
    #word_letters - letters for word
    #word_list - Dashes

    word = get_valid_word(words)
    print(word)
    word_letters = set(word.lower()) # letters in the word
    alphabet = set(string.ascii_lowercase)
    used_letters = set() # what the user has guess
   
    # getting user input
    while len(word_letters) > 0:
        # letters used
        # ' ' .join['a', 'b', 'cd'] ---> 'a b cd"
        print('You have used these letters: ', ' '.join(used_letters))
        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').lower()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print('You already guessed this letter. Please try again.')

        else:
            print('Invalid character. Please try again.')
        
    # gets here when len(word_letters) == 0


hangman()