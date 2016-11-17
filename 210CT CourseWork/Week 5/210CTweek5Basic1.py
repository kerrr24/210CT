numlist = str(input("List of Numbers (With space between them): "))
numlistsplit = numlist.split(" ")
numlistsplit.append("")
listLen = len(numlistsplit)

def longSub(i, longestList, multiple):

    print("Current best: " + str(longestList))
    lengList = [numlistsplit[i-1]]

    while i < listLen:

        if numlistsplit[i] > numlistsplit[i-1]:
            lengList.append(numlistsplit[i])
            i = i + 1
            
        elif numlistsplit[i] < numlistsplit[i-1]:
            
            if len(lengList) > len(longestList):
                
                i = i + 1
                longestList = lengList
                longSub(i, lengList, multiple)
  
            else:
                break;
            
        else:
            i = i + 1
            longSub(i, longestList, multiple)
            
longSub(1, [], [])
