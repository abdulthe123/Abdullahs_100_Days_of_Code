print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("note: Please answer each question in one word")
print("""You wake up from your slumber to see two paths on either side of you, 
one on your right and one on your left. """)

direction = input("Would you like to go left or right? ")
movement = "placeholder"

if  direction == "Left" or direction == "left":
    print("You walk down the path to your left and reach a lake on the "
          "island. You see a boat approaching in the distance, but you also "
          "are very impatient.")

    movement = input("Would you like to swim across the lake now or wait for "
                     "the boat to arrive? ")
    if movement == "Wait" or movement == "wait":
        print("You wait and board the boat, and as soon as you cross the lake you "
              "reach a temple and enter it. You are now surrounded by three doors."
              " One of the doors is blue, the second yellow, and the third red")
        door_choice = input(
            "Would you like to enter the red, blue, or yellow door? ")
        if door_choice == "Blue" or door_choice == "blue":
            print("You walk through the door and are ripped to shreds by a "
                  "pack of wolves :( Game over, better luck next time! ")
        elif door_choice == "Red" or door_choice == "red":
            print("You walk through the door and fall into an abyss of flames "
                  ":( Game over, better luck next time! ")
        elif door_choice == "Yellow" or door_choice == "yellow":
            print("You step through the door and are greeted with the sight of a "
                  "giant treasure chest laden with gold. Congratulations, "
                  "you have found the treasure!")
        else:
            print("You are teleported into a different dimension and instantly are snuffed from "
                  "existence. :( Game over, better luck next time!")
    else:
        print("You tried to swim across but unfortunately a giant trout "
              "swallowed you whole and you died. ")
else:
    print("You set out on the path to your right and start walking, only to "
          "fall into a hidden hole and instantly die. :( Game Over, better "
          "luck next time! ")