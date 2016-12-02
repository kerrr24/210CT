userList = input("Enter values with spaces between: ")
userList = userList.split()
lowestPara = int(input("Lowest Parameter: "))
highestPara = int(input("Highest Parameter: "))


def binarySearch(array):

    lowest = 0
    highest = len(userList) - 1
    midPointStopper = -1 #used as a value to stop the loop, stops if statements from running


    while True: #loop runs forever until a break occurs

            midPoint = (lowest + highest) // 2 #finds the mid point
            print(midPoint)
            
            if int(array[midPoint]) < lowestPara and midPointStopper != midPoint:
                lowest = midPoint + 1
                midPointStopper = midPoint #sets the stopper to the value of the midPoint so that if the same midPoiint is used again then the if statment won't run as it implies that no element from the list is between the parameters as all midPoints have been used
                
            elif int(array[midPoint]) > highestPara and midPointStopper != midPoint:
                highest = midPoint - 1
                mipPointStopper = midPoint #sets the stopper to the value of the midPoint so that if the same midPoiint is used again then the if statment won't run as it implies that no element from the list is between the parameters as all midPoints have been used
                
            elif int(highestPara) >= int(array[midPoint]) and int(lowestPara) <= int(array[midPoint]): #checks to see if midPoint is between both parameter set by the user
                 print(" A value is in the array between " + str(lowestPara) + " and " + str(highestPara))
                 break; #stops the loop

            else:     
                print("No Valuse Present Between Given Parameters")
                break; #stops the loop

                
        
            
binarySearch(userList)
