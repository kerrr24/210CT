origSentence = str(input("Sentence: "))
wordList = origSentence.split() #splits sentence at a space and creates a list using them
print(wordList)
listLen = len(wordList)
i = 0

while i < (listLen/2):
    temp = wordList[i] #gets the value of the word from location i
    wordList[i] = wordList[listLen-(i + 1)] #changes word in location i to word from location from word from location (i away from end) 
    wordList[listLen-(i + 1)] = temp #sets word in (i away from end) to the temp value create two lines up
    i = i + 1

revWordList = " ".join(wordList) #combines words in list by adding spaces between them
print(revWordList)
