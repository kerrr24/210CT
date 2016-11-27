numlist = str(input("List of Numbers (With space between them): "))
numlistsplit = numlist.split(" ") #splits numbers on spaces also creates list
numlistsplit.append("")
listLen = len(numlistsplit)
oneormeore = False


def longSub(i, longestList):

    print("Current best: " + str(longestList))
    lengList = [numlistsplit[i-1]]

    while i < listLen:

        if numlistsplit[i] > numlistsplit[i-1]: #if the current element is greater than the previous element in the list then the followigng code runs
            lengList.append(numlistsplit[i]) #adds number at postion i to list of current length check
            i = i + 1
            
        elif numlistsplit[i] < numlistsplit[i-1]: #if current element less than previous element then following code runs
            
            if len(lengList) > len(longestList): #if the length of the current list is greater than the longestpossible then the following code runs
                
                i = i + 1
                longestList = lengList #sets longestlist to the current list being made
                longSub(i, lengList)# recursive call with updated values
  
            else:
                break; #stops loop
            
        else:
            i = i + 1
            longSub(i, longestList) #recursive call with updated values
            
longSub(1, [])
