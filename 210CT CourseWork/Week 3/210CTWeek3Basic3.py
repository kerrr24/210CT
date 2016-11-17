wordVowel = input("Enter Word: ")
wordVowelList = list(wordVowel)
wordVowelList.append("")
endlen = len(wordVowelList) - 1
count = 0


def vowelRemover(count, letter):
    if count < endlen:
        if wordVowelList[count] in "aeiouAEIOU":
            wordVowelList.remove(wordVowelList[count])
            global endlen
            endlen = endlen - 1
            vowelRemover(count, wordVowelList[count])
            
        elif wordVowelList[count] not in "aeiouAEIOU":
            count = count + 1
            vowelRemover(count, wordVowelList[count])
            
        else:
            pass
            
    else:
        vowellessWord = "".join(wordVowelList)
        print(vowellessWord)

vowelRemover(count, wordVowelList[count])

