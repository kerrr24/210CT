wordVowel = input("Enter Word: ")
wordVowelList = list(wordVowel) #creates list using the word the user entered
wordVowelList.append("")
endlen = len(wordVowelList) - 1
count = 0

def vowelRemover(count, letter):
    if count < endlen:
        if wordVowelList[count] in "aeiouAEIOU": #checks if selected letter is in the string aeiouAEIOU, meaing any vowels will be removed 
            wordVowelList.remove(wordVowelList[count])
            global endlen
            endlen = endlen - 1
            vowelRemover(count, wordVowelList[count]) #recurive call with updated values
            
        elif wordVowelList[count] not in "aeiouAEIOU": #checks if selected letter is not in the string aeiouAEIOU
            count = count + 1
            vowelRemover(count, wordVowelList[count]) #recurive call with updated values
            
        else:
            pass
            
    else:
        vowellessWord = "".join(wordVowelList) #combines all the letters in the list without any space
        print(vowellessWord)

vowelRemover(count, wordVowelList[count])
