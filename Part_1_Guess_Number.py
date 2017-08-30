import random

def main():
    randomNumber = random.randint(1, 10)
    print("Greetings! Pick a number, any number ")
    print("between 1 and 10.")

    while True:
        usersChoice = int(input())
        correctChoice = compareValues(randomNumber, usersChoice)
        if correctChoice == True:
            break

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