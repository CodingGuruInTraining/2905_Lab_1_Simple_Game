# This program runs a simple guessing game.

# Import random library
import random

def main():
    # Gets a random number between 1 and 10
    randomNumber = random.randint(1, 10)
    # Displays introduction message and instruction
    print("Greetings! Pick a number, any number ")
    print("between 1 and 10.")

    # Continues asking User for input till the correct
    # Answer is given
    while True:
        usersChoice = int(input())
        correctChoice = compareValues(randomNumber, usersChoice)
        # Breaks loop if correct choice is made
        if correctChoice == True:
            break

# Function that compares values and displays result.
def compareValues(randomNumber, userChoice):
    correct = False
    if randomNumber == userChoice:
        correct = True
        print("Correct!")
    elif randomNumber > userChoice:
        print("Nope, too low.")
    else:
        print("Nope, too high.")
    return correct

main()