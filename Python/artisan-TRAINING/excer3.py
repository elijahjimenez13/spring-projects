def stringDestroyer():
    word = input('Input a STRING: ')
    word = [*word]
    print(word[1::2]) # [start:stop:step]

sadge = stringDestroyer()