import random
import os

library = ["hello","world", 'god', 'dog', 'cat', 'bird', 'hawk', 'pantheon', 'minecraft', 'skyrim', 'table', 'chair', 'game', 'war', 'wall', 'astartes']

def welcomeMsg():
    print("Welcome to Hangman!")
    print("Your job is to guess the word before your turns run out!")
    print("Be Careful! if you guess the word early and you're wrong, YOU LOSE!")
    print("So take your time and think things over before giving an answer.")
    

def resetCli():
    if os.name == "nt":
        os.system("cls")
    else: os.system("clear")

def restart():
    if input("\n Wanna try again? [y/n]") == "y":
        resetCli()
        game()

def endGame():
    resetCli()
    print("THANKS FOR PLAYING!")

def findOccurence(word, char):
    return [index for index, letter in enumerate(word) if letter == char]

def inputIsValid(inp):
    if inp.isdigit() or not inp.isalpha():
        return False
    else: return True
    
def game():
    target = random.choice(library)
    progress = '-' * len(target)
    guesses = ''
    turns = len(target) + 2

    seperator = "--" * 15

    wrong_guess = False
    right_guess = False
    invalid = False

    while turns >= 0:
        resetCli()

        print(seperator)
        print(f"Your word is: {progress}\nYour attempts {guesses} \nTurns left: {turns}")

        # Messages
        if wrong_guess:
            print(seperator)
            print('Sry, not in the word!')
            print(seperator)
            wrong_guess = False
        if right_guess:
            print(seperator)
            print('Good Job!')
            print(seperator)
            right_guess = False
        if invalid:
            print(seperator)
            print("Invalid Input!")
            print(seperator)
        print()

        inp = input(f'Your guess: ')

        # Guessing the Word
        if len(inp) > 1:
            if inp == target:
                print("CONGRATULATIONS! YOU WON!")
                print(f"Number of attempts: {len(target) - turns + 1}")    
                break
            else:
                print("You Lost.")
                print(f"Your word was: {target}")
                break

        # Input Validity
        if not inputIsValid(inp) or inp in guesses:
            invalid = True

            continue

        
        # Guessing Characters
        if inp in target:
                indices = findOccurence(target,inp)
                for i in indices:
                    progress = progress[:i] + inp + progress[i+1:]
                guesses += inp
                right_guess = True
        else:
            guesses += inp
            wrong_guess = True
            
        
        turns -= 1

    if turns <= 0:
        print("You Lose!")

    restart()


def main():
    resetCli()

    welcomeMsg()
    print()
    if input('Ready to Start? [y/n]') == "y":
        game()

main()
