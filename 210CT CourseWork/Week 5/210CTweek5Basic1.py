numlist = str(input("List of Numbers (With space between them): "))
numlistsplit = numlist.split(" ") #splits numbers on spaces also creates list
numlistsplit.append("")
listLen = len(numlistsplit) - 1
done = False


def longSub(count, longestList, currentList):
    
    i = count
    lengList = currentList
    print("Current best: " + str(longestList))
    done = False

    while i < listLen + 1 and done == False:


      if numlistsplit[i] != "" and done == False:


            if int(numlistsplit[i]) >= int(numlistsplit[i-1]): #if the current element is greater than the previous element in the list then the followigng code runs
                i = i + 1
                lengList.append(numlistsplit[i-1]) #adds number at postion i to list of current length check
                #print("added: " + str(numlistsplit[i-1]))

                if i > listLen:
                    break;
                
            elif int(numlistsplit[i]) < int(numlistsplit[i-1]): #if current element less than previous element then following code runs

                #print("LengList: " + str(len(lengList)))
                #print("longestList: "+ str(len(longestList)))
                
                if int(len(lengList)) > int(len(longestList)): #if the length of the current list is greater than the longestpossible then the following code runs
                    
                    i = i + 1
                    #print(i)
                    print("New Best")
                    longestList = lengList #sets longestlist to the current list being made
                    print(longestList)
                    longSub(i, longestList, list(numlistsplit[i - 1]))# recursive call with updated values
                    
                else:
                    i = i + 1
                    #print(i)
                    longSub(i, longestList, list(numlistsplit[i - 1]))

      else:
            if int(len(lengList)) > int(len(longestList)): #if the length of the current list is greater than the longestpossible then the following code runs
                    i = i + 1
                    print("New Best")
                    longestList = lengList #sets longestlist to the current list being made
                    print(longestList)

            print("Longest Possible: " + str(longestList))
            global done
            done = True


print(listLen)
      
longSub(1, [], list(numlistsplit[0]))
