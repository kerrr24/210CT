userEnd = "Y"
startSafe = False
lengthSafe = False

while userEnd == "Y":
    startWord = input("Word to be cut: ")
    wordlength = len(startWord) - 1
    
    while startSafe == False:
        cutStart = input("How far in cut will start (0 to " + str(wordlength) + "): ")
        if int(cutStart) < 0 or int(cutStart) > wordlength:
            print("START POSTION MUST BE BETWEEN 0 AND " + str(wordlength))
        else:
            startSafe = True
            cutlengthPosi = wordlength - int(cutStart)
            
    while lengthSafe == False:       
        cutLength = input("length of cut (1 to to " + str(cutlengthPosi) + "): ")
        if int(cutLength) < 1 or int(cutLength) > cutlengthPosi:
             print("CUT LENGTH MUST BE BETWEEN 1 AND " + str(cutlengthPosi))
        else:
            lengthSafe = True
            cutend = int(cutStart) + int(cutLength)
            

    convetList = list(startWord)
    convetList[int(cutStart):int(cutend)] = []
    endWord = "".join(convetList)
    print("Word is now: "+ str(endWord))
    

    startSafe = False
    lengthSafe = False

    userEnd = input("Start new (Y/N)")

