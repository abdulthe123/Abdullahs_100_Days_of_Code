"""
Number Guessing Game
Computer selects a number between 1 and 100
player has choice of hard or easy mode
hard mode gives the player 5 chances to guess the number
easy mode gives the player 10 chances
for each guess, the game will tell the user if their guess is higher than or lower than the number
"""
import random

print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

def game_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "hard":
        return level
    elif level == "easy":
        return level
    else:
        return "Invalid Input"
    
level = game_difficulty()
    
target_number = random.randint(1,100)
guesses = 10

def gameflow():
    global target_number
    global guesses
    global level
    you_lose = False

    if level == "hard":
        guesses = 5

    print(f"You have {guesses} attempts to guess the number")
    # Guessing loop
    while you_lose == False:
        guess = int(input("Make a guess:"))
        if guess == target_number:
            return "Success"
        elif guess < target_number:
            print("Too Low.")
            guesses -= 1
        elif guess > target_number:
            print("Too High.")
            guesses -= 1
        if guesses == 0:
            you_lose = True
            return "Failure"


result = gameflow()

if result == "Success":
    print("Congratulations, you guessed the number!")
elif result == "Failure":
    print("You ran out of guesses :(, better luck next time.")