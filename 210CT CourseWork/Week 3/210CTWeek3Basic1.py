origSentence = str(input("Sentence: "))
wordList = origSentence.split()
print(wordList)
listLen = len(wordList)
i = 0

while i < (listLen/2):
    temp = wordList[i]
    wordList[i] = wordList[listLen-(i + 1)]
    wordList[listLen-(i + 1)] = temp
    i = i + 1

revWordList = " ".join(wordList)
print(revWordList)
