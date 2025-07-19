#access libraries and py files
import spiderDraw as sd
import functions as md
import os
import time
#Initialize variables and setup
#Need to keep track of correct letters, incorrect letters and tries
tries = 0
correct_letters = []
incorrect_letters = []
secret_word = ""
game = True
#Make a list of the spider drawings
spiderList = [
    sd.spider_0, sd.spider_1, sd.spider_2, sd.spider_3, sd.spider_4,
    sd.spider_5, sd.spider_6
]

#Print intro statements (welcome to game, etc)
name = input("What is your name?")
md.introduction("Welcome to the Spider guess Game!", name)

#generate a random word from word list
secret_word = md.generate_word()

#Game Loop
while game:
    #This is where you'll call all of your functions. Just need to decide the tyouproper order.
    progress = ''
    tries = md.check_word(correct_letters, incorrect_letters, secret_word,
                          tries)
    time.sleep(1)
    os.system('clear')
    progress = md.print_word(secret_word, correct_letters)
    print(f'Word = {progress}')
    md.print_spider(tries, spiderList)
    print(f'Incorrect guesses = {incorrect_letters}')

    #You will also need to specify your win and lose conditions in here
    if progress == secret_word or '_' not in progress:
        print('You win!')
        game = False
        rematch = input('Would you like to play again?')
        if rematch == 'yes':
            game = True
            tries = 0
            correct_letters = []
            incorrect_letters = []
            secret_word = md.generate_word()
        else:
            print("Thanks for playing!")

    elif tries > 5:
        print('You lose!')
        game = False
        rematch = input('Would you like to play again?')
        if rematch == 'yes':
            game = True
            tries = 0
            correct_letters = []
            incorrect_letters = []
            secret_word = md.generate_word()
        else:
            print("Thanks for playing!")
