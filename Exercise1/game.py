# Kian Candelario
import random

def picks(pick):
    if (pick == 1):
        return "Rock"
    elif (pick == 2):
        return "Paper"
    elif (pick == 3):
        return "Scissors"

def possibleOutcomes(userPick, opponent):
    '''
        1 - Rock
        2 - Paper
        3 - Scissors
    '''
    # Rock possible outcomes
    if (userPick == 1):
        if (userPick == 1 and opponent == 1):
            return "Draw!"
        elif (userPick == 1 and opponent == 2):
            return "You lose!"
        elif (userPick == 1 and opponent == 3):
            return "You win!"

    # Paper possible outcomes
    elif (userPick == 2):
        if (userPick == 2 and opponent == 1):
            return "You win!"
        elif (userPick == 2 and opponent == 2):
            return "Draw!"
        elif (userPick == 2 and opponent == 3):
            return "You lose!"
    
    # Scissors possible outcomes
    elif (userPick == 3):
        if (userPick == 3 and opponent == 1):
            return "You lose!"
        elif (userPick == 3 and opponent == 2):
            return "You win!"
        elif (userPick == 3 and opponent == 3):
            return "Draw!"

def rockPaperScissors():
    print("Welcome to Rock, Paper, and Scissors Game")
    print('''
        Press [1] for Rock
        Press [2] for Paper
        Press [3] for Scissors
    ''')
    print("")
    userPick = int(input("[1] Rock | [2] Paper | [3] Scissors: "))
    opponentPick = random.randint(1,3)

    print("")
    print(f"You: {picks(userPick)}")
    print(f"Opponent: {picks(opponentPick)}")
    print(f"Result: {possibleOutcomes(userPick, opponentPick)}")

rockPaperScissors() # Function call