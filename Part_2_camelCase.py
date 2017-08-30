def main():
    sentence = "fOnt proCESSOR and ParsER".lower()
    badCharsList = ["@", "#", "$", "%", "^", "&", "*"]
    for badChar in badCharsList:
        if badChar in sentence:
            print("WARNING! Bad Character found!")

    separateWords = sentence.split()
    newSentence = ""
    for i in range(0, len(separateWords)):
        if i > 0:
            newSentence += separateWords[i][0].upper()
            newSentence += separateWords[i][1:]
        else:
            newSentence += separateWords[i]
    print(newSentence)
main()