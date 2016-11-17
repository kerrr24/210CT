numlist = str(input("List of Numbers (With space between them): "))
numlistsplit = numlist.split(" ")
print(numlistsplit)
listLen = len(numlistsplit)


def longSub(i, bestLen, bestLastNum, bestFirstNum, setUp):

    if setUp == False:
        firstNum = i - 1
        lastNum = i
        count = i
        lenDict = {}

    while i < listLen:

        if numlistsplit[i] > numlistsplit[i-1]:
            count = i + 1
            lastNum = i
            bestLastNum = i
            #lenDict[bestLen] = bestFirstNum
            
        elif numlistsplit[i] < numlistsplit[i-1]:
            
            if (lastNum - firstNum) > bestLen or (lastNum - firstNum) == bestLen:
                
                bestLen = lastNum - firstNum
                bestFirstNum = bestLastNum - bestLen
                #lenDict[bestLen] = bestFirstNum
                longSub(i, bestLen, bestLastNum, bestFirstNum, True)
                #print(lenDict)
                i = i + 1
                
            else:
                #print("HERE")
                break;
            
        else:
            lastNum = i
            bestLastNum = i
            bestFirstNum = 0
            #lenDict[bestLen] = bestFirstNum
            i = i + 1
            longSub(i, bestLen, bestLastNum, bestFirstNum, True)
        

    print(numlistsplit[bestFirstNum:bestLastNum])
    

longSub(1, 0, 0, 0, False)
