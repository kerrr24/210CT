userList = input("Enter values with spaces between: ")
userList = userList.split()
lowestPara = int(input("Lowest Parameter: "))
highestPara = int(input("Highest Parameter: "))


def binarySearch(array):

    lowest = 0
    highest = len(userList) - 1
    midPointStopper = -1


    while True:

            midPoint = (lowest + highest) // 2
            
            if int(array[midPoint]) < lowestPara and midPointStopper != midPoint:
                lowest = midPoint + 1
                midPointStopper = midPoint
                
            elif int(array[midPoint]) > highestPara and midPointStopper != midPoint:
                highest = midPoint - 1
                mipPointStopper = midPoint
                
            elif str(highestPara) > array[midPoint] and str(lowestPara) < array[midPoint]:
                 print(" A value is in the array between " + str(lowestPara) + " and " + str(highestPara))
                 break;

            else:     
                print("No Valuse Present Between Given Parameters")
                break;
        
            
binarySearch(userList)
