userList = input("Enter values with spaces between: ")
userList = userList.split()
#findelem = int(input("Number to check for: "))
lowestPara = int(input("Lowest Parameter: "))
highestPara = int(input("Highest Parameter: "))
done = False


def binarySearch(array, findelem, highestPara, isdone):

    lowest = 0
    sequenceList = userList
    highest = len(userList)

    if isdone == False and findelem != highestPara:

        print(findelem)

        if findelem <= highestPara:

            while len(sequenceList) > 0:

                midPoint = (lowest + highest) // 2
                if str(findelem) > array[midPoint]:
                    lowest = midPoint + 1
                    sequenceList = sequenceList[lowest:highest]
                elif str(findelem) < array[midPoint]:
                    highest = midPoint - 1
                    sequenceList = sequenceList[lowest:highest]
                else:
                    print(" A value is in the array between " + str(lowestPara) + " and " + str(highestPara))
                    global done
                    done = True
                    break;


                binarySearch(userList, findelem + 1, highestPara, done)


    else:
        pass;
            
binarySearch(userList, lowestPara, highestPara, False)
