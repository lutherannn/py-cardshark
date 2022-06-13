import random, os, traceback
from sys import exit

deck = [
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
]


def writeScore():
    global cardLine
    prompt = input("Would you like to save this score (y/n)? ")

    if prompt == "y" or prompt == "yes":
        username = input("Name: ")
        try:
            with open("scores.txt", "a") as f:
                f.write(f"{username}: {str(len(cardLine) - 1)}")
                f.write("\n")
                f.close()
        except:
            print(traceback.format_exc())
        
        try:
            with open("scores.txt", "r") as f:
                scores = f.readlines()
                f.close()
                print("\n".join(scores))
        except:
            print(traceback.format_exc())

def clear():
    os.system("cls" if os.name == "nt" else "clear")


def instructions():
    print("Welcome to Card Sharks")
    print(
        "You will be given a starting card, you must then decide if the next card will be higher or lower"
    )
    print("Aces are always high")
    print("If the card is the same value, then it counts as a free pass")
    print("See how far you can go! Press enter to begin.")
    os.system("pause" if os.name == "nt" else 'read -p ""')

def gameLoop():
    global cardLine
    clear()
    lost = False
    cardLine = []
    card = random.choice(deck)
    cardLine.append(card)
    deck.remove(card)

    while not lost:
        print(f"Cards: {cardLine}")
        nextCard = random.choice(deck)
        deck.remove(nextCard)

        action = input("(H)igher or (L)ower> ").lower()
        if action == "h" or action == "higher":
            if cardLine[-1] > nextCard:
                lost = True
                print(f"You lost! The next card was: {nextCard}")
                print(f"You scored: {len(cardLine) - 1}")
                writeScore()
            cardLine.append(nextCard)

        if action == "l" or action == "lower":
            if cardLine[-1] < nextCard:
                lost = True
                print(f"You lost! The next card was: {nextCard}")
                print(f"You scored: {len(cardLine) - 1}")
                writeScore()
            cardLine.append(nextCard)

instructions()
gameLoop()
