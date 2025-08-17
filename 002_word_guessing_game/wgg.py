# game
    # generate a random word
    # player guesses a character
        # if its in the word, replace "_" with the said character
        # else, take a turn away

import random
import os

words = ["Hello", "World", "Apple", "Orange", "Book", "Sideways", "Pantheon", "God", "Dog", "People", "Animal"]


def restart():
    if input("Try Again? [y/n]") == "y":
        game(words)

def findOccurence(word, character):
    return [i for i, letter in enumerate(word) if letter == character]

def game(words):
    answer = random.choice(words).lower()
    guesses = "" #store all guessed characters
    progress = "-" * len(answer) #shows all correctly guessed characters and their positions
    turns = 5

    print("Alright! lets begin.")
    while turns >= 0:
        print(f"Your word: {progress}")
        guess = input("Your guess?  ")
        if len(guess) > 1 and guess == answer:
            print("Congratulations! you win!")
            print(f"Number of guesses: {5 - turns}")
            break
        elif len(guess) >1 and guess != answer:
            print("You Lost!")
            print(f"Your Word was [{answer}]")
            break

        occ = findOccurence(answer, guess)
        if len(occ) == 0:
            print("sry, not in it.\n")
            turns -= 1
        else:
            for i in occ:
                progress = progress[0:i] + guess + progress[i+1:]
                print("")
            turns -= 1

    if turns == 0:
        print("You Lose!")   
        print(f"your word was {answer}\n")
    

    restart()

    


def main():
    # Clear the terminal
    if os.name == "nt": 
        os.system("cls")
    else: os.system("clear")

    print("Hi! Welcome to word guessing game!")
    print("I will give you a word, and you'll try to guess it!")
    print("remember, you have only 5 turns, and guessing a full word means if you're wrong, you'll lose!")
    print("so tread carefully!")
    
    if input("\nReady to begin?[y/n]") == "y":
        game(words)
    
    print("very well, see you next time!")

main()
