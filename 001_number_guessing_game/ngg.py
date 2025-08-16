import random 

def answer_rng():
    rng: int = (random.randint(0,500), random.randint(0,500))
    answer: int = random.randrange(min(rng),max(rng))

    return rng, answer

def check_answer(guess, answer, rng):
    if not guess.isdigit() or int(guess) > max(rng) or int(guess) < min(rng):
        print("Invalid answer!")
        return False
    if answer == int(guess): return True
    if answer < int(guess) : 
        print("Too High. Try again!")
        return False
    else:
        print("Too Low. Try again!")
        return False

def game_loop():
    rng,answer = answer_rng()
    guess_count = 0
    print(f"your number is between {min(rng)} and {max(rng)}")
    while True:
        if check_answer(input("Your Guess: "), answer, rng):
            print("Congratulation! You Won!")
            print(f"Number of Guesses : {guess_count + 1}")
            break
        else:
            guess_count += 1

    
    print()
    if input("Restart? [y/n]\n") == "y":
        game_loop()

def main():
    print("hi! Welcome to my number guessing game!")
    print("In this game, i give a rng of numbers, and you need to guess what the number is!")
    print("Your goal is to find the number in the least amount of guesses possible!")
    print()
    print()
    
    if input("Ready? [y,n]\n") == "y":
        game_loop()


main()



