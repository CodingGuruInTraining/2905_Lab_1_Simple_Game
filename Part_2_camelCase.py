# This program converts a string into a camel case jumble.

def main():
    # Static string, but can be replaced with input()
    # Sentence is set to lowercase to start with
    sentence = "fOnt proCESSOR and ParsER".lower()
    # Static list of possible bad characters
    badCharsList = ["@", "#", "$", "%", "^", "&", "*"]
    # Loops through list and checks if in sentence
    for badChar in badCharsList:
        if badChar in sentence:
            print("WARNING! Bad Character found!")
            break
    # Splits sentence string into array
    separateWords = sentence.split()
    newSentence = ""
    # Loops through array, capitalizes the first letter,
    # then adds remaining characters to a combined string
    # variable
    for i in range(0, len(separateWords)):
        if i > 0:
            newSentence += separateWords[i][0].upper()
            newSentence += separateWords[i][1:]
        else:
            newSentence += separateWords[i]
    print(newSentence)
main()