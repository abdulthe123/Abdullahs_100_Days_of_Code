import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# I need to first build logic that randomly generates a choice from the computer
# Then I can compare that to the user selected choice
# And then i can evaluate the winner based on that

print("Let's play rock, paper, scissors! ")
player_choice = input("Rock, Paper, or Scissors?\n").lower()

print(f"\nPlayer 1 has selected {player_choice}!\n")

if player_choice == "rock":
    print(rock)
elif player_choice == "paper":
    print(paper)
elif player_choice == "scissors":
    print(scissors)
else:
    print("Haha you suck try again")

choice_options = [rock, paper, scissors]
selection = random.randint(0, 2)
computer_choice = choice_options[selection]
translation = "blank"
if computer_choice == rock:
    translation = "rock"
elif computer_choice == paper:
    translation = "paper"
elif computer_choice == scissors:
    translation = scissors

print(f"\nThe computer has chosen {translation}!\n{computer_choice}")

if player_choice == "rock":
    if computer_choice == paper:
        print("The computer wins!")
    elif computer_choice == scissors:
        print("You win!")
    elif computer_choice == rock:
        print("It's a tie! Try again")
elif player_choice == "paper":
    if computer_choice == scissors:
        print("The computer wins!")
    elif computer_choice == rock:
        print("You win!")
    elif computer_choice == paper:
        print("It's a tie! Try again")
elif player_choice == "scissors":
    if computer_choice == rock:
        print("The computer wins!")
    elif computer_choice == paper:
        print("You win!")
    elif computer_choice == scissors:
        print("It's a tie! Try again")


