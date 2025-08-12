logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computerchoice = random.choice(cards)
playerhand = random.sample(cards, 2)
playerscore = sum(playerhand)
computerhand = [computerchoice]
computerscore = sum(computerhand)

def hitorstand():
    global playerhand
    global computerhand
    global computerscore
    global playerscore

    while not playerscore > 21:
        hitchoice = input("Type 'y' to get another card, type 'n' to pass: ")
        if hitchoice == "y":
            newcard = random.choice(cards)

            if newcard == 11 and newcard + playerscore > 21:
                newcard = 1

            playerhand.append(newcard)
            playerscore = sum(playerhand)

            if playerscore == 21:
                return "Blackjack!"
            if playerscore > 21:
                playerscore = sum(playerhand)
                return playerhand

            print(f"\nYour cards: {playerhand}, current score: {playerscore}\nComputers first " 
                  f"card: "
                  f"{computerhand}\n")

        if hitchoice == "n":
            while computerscore < 17:
                dealercard = random.choice(cards)

                if dealercard == 11 and dealercard + computerscore > 21:
                    dealercard = 1

                computerhand.append(dealercard)
                computerscore = sum(computerhand)

            return computerhand

def game():
    global playerhand
    global computerhand
    global computerscore
    global playerscore
    print("\n"*20 + logo)
    print(f"\nYour cards: {playerhand}, current score: {playerscore}\nComputers first card: "
          f"{computerhand}\n")

    round1 = hitorstand()

    if round1 == "Blackjack!":
        return (f"\nYour final hand: {playerhand}, final score: {playerscore}\nDealer's "
                f"final hand: {computerhand}, final score: {computerscore}\nBlackjack! You win!.\n")
    elif round1 == playerhand:
        return (f"\nYour final hand: {playerhand}, final score: {playerscore}\nDealer's "
                f"final hand: {computerhand}, final score: {computerscore}\nGame over, you bust.\n")
    elif round1 == computerhand:
        if computerscore > 21:
            return (f"\nYour final hand: {playerhand}, final score: {playerscore}\nComputer's "
                    f"final hand: {computerhand}, final score: {computerscore}\nGame over, "
                    f"Dealer bust, You Win!\n")
        elif computerscore > playerscore:
            return (f"\nYour final hand: {playerhand}, final score: {playerscore}\nComputer's "
                    f"final hand: {computerhand}, final score: {computerscore}\nGame over, "
                    f"Dealer wins.\n")
        elif playerscore > computerscore:
            return (f"\nYour final hand: {playerhand}, final score: {playerscore}\nComputer's "
                    f"final hand: {computerhand}, final score: {computerscore}\nGame over, "
                    f"You win!\n")
        elif playerscore == computerscore:
            return (f"\nYour final hand: {playerhand}, final score: {playerscore}\nComputer's "
                    f"final hand: {computerhand}, final score: {computerscore}\nGame over, "
                    f"Tie!\n")
    return None

def play():
    global playerhand
    global computerhand
    global computerscore
    global playerscore
    global computerchoice

    endgame = False
    while not endgame:
        question = input("Do you want to play a game of Blackjack? 'y' or 'n' ")
        if question == "y":
            print(game())
            playerhand.clear()
            computerhand.clear()
            computerchoice = random.choice(cards)
            playerhand = random.sample(cards, 2)
            playerscore = sum(playerhand)
            computerhand = [computerchoice]
            computerscore = sum(computerhand)

        elif question == "n":
            endgame = True



play()

