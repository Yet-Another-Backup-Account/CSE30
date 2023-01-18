# assignment: programming assignment 1
# author: Pranav Jha
# date: 2023-01-17 (YYYY-MM-DD) @ 14:33 Pacific Standard Time (PST)
# file: hangman.py is a program that lets you play a text based version of the game hangman
# input: you can input the size of the word, the amount of lives and guesses
# output: the lives left, and the guesses that have been made already

from random import choice, random

dictionary_file = "dictionary.txt"   # make a dictionary.txt in the same folder where hangman.py is located

# write all your functions here
def game_reset():
    global word, guess_list, blanks, blanklist, lives_lost, olist
    word = choice(dictionary[size])
    guess_list = []
    blanks = '__ ' * size
    blanklist = blanks.split()
    olist = list('O' * lives)
    if '-' in word:
        for index, letter in enumerate(list(word)):
            if letter == '-':       
                blanklist[index] = '-'
    lives_lost = 0                

def interface(guess_list, blanklist, olist):
    guesses = ' '.join(word.upper() for word in guess_list)
    blanks = ' '.join(blank for blank in blanklist)
    o = ''.join(o for o in olist)
    print(f'Letters chosen: {guesses}')
    print(f'{blanks}    lives: {lives} {o}')

# make a dictionary from a dictionary file ('dictionary.txt', see above)
# dictionary keys are word sizes (1, 2, 3, 4, …, 12), and values are lists of words
# for example, dictionary = { 2 : ['Ms', 'ad'], 3 : ['cat', 'dog', 'sun'] }
# if a word has the size more than 12 letters, put it into the list with the key equal to 12
def import_dictionary (filename) :
    dictionary = {}
    max_size = 12
    try :
        with open(filename, 'r') as file:
            words = file.readlines()
            for i in range(1, max_size+1):
                l = []
                for word in words:
                    if len(word.strip()) == i:
                        l.append(word.strip())
                    elif i == 12:
                        len(word.strip()) >= 12
                if l != []:
                    dictionary[i] = l
    except Exception :
        pass
    return dictionary

# print the dictionary (use only for debugging)
def print_dictionary (dictionary) :
    max_size = 12
    try:
        if max(dictionary.keys()) == max_size:
            print(dictionary)
            return True
    except:
        return False

# get options size and lives from the user, use try-except statements for wrong input
def get_game_options () :
    try:
        size = int(input("Please choose a size of a word to be guessed [3 – 12, default any size]: "))
    except:
        size = choice(list(range(3, 13)))
    print(f'The word size is set to {size}.')
    try:
        lives = int(input("Please choose a number of lives [1 – 10, default 5]: "))
        assert int(lives) > 0
    except:
        lives = 5
    print(f'You have {lives} lives.')
    return size, lives

# MAIN

if __name__ == '__main__' :

    # make a dictionary from a dictionary file
    dictionary = import_dictionary(dictionary_file)

    # print the dictionary (use only for debugging)
    #print_dictionary(dictionary)    # remove after debugging the dictionary function import_dictionary

    # print a game introduction
    print("Welcome to the Hangman Game!")

    # START MAIN LOOP (OUTER PROGRAM LOOP)
    # set up game options (the word size and number of lives)
    size, lives = get_game_options()

    # select a word from a dictionary (according to the game options)
    # use choice() function that selects an item from a list randomly, for example:
    # mylist = ['apple', 'banana', 'orange', 'strawberry']
    # word = choice(mylist)
    game_reset()
    
    # START GAME LOOP   (INNER PROGRAM LOOP)
    while True:
        # format and print the game interface:
        # Letters chosen: E, S, P                list of chosen letters
        # __ P P __ E    lives: 4   XOOOO        hidden word and lives
        interface(guess_list, blanklist, olist)

        # ask the user to guess a letter
        while True:
            try:
                guess = input("Please choose a new letter > ")
                if len(guess) != 1 or not guess.isalpha() or guess in guess_list:
                    assert 1 == 0
                else:
                    break
            except:
                if guess in guess_list:
                    print('You have already chosen this letter.')

        # update the list of chosen letters
        guess_list.append(guess)

        # if the letter is correct update the hidden word,
        # else update the number of lives
        # and print interactive messages
        # also check if the user guesses the word correctly or lost all lives,
        # if yes finish the game
        if guess.lower() in word.lower():
            print("You guessed right!")
            for index, letter in enumerate(list(word.lower())):
                if letter == guess:
                    blanklist[index] = letter
        else:
            lives -= 1
            olist[lives_lost] = 'X'
            lives_lost += 1
            print("You guessed wrong, you lost one life.")
                

        # END GAME LOOP   (INNER PROGRAM LOOP)

        # ask if the user wants to continue playing.
        # if yes start a new game, otherwise terminate the program
        if '__' not in blanklist or lives == 0:
            if '__' not in blanklist:
                print(f'Congratulations!!! You won! The word is {word.upper()}!')
                replay = input("Would you like to play again [Y/N]? ")
                if replay.lower() == 'y':
                    size, lives = get_game_options()
                    game_reset()
                    continue
                else:
                    print('Goodbye!')
                    break
            elif lives == 0:
                print(f'You lost! The word is {word.upper()}!')
                replay = input("Would you like to play again [Y/N]? ")
                if replay.lower() == 'y':
                    size, lives = get_game_options()
                    game_reset()
                    continue
                else:
                    print('Goodbye!')
                    break

    # END MAIN LOOP (OUTER PROGRAM LOOP)