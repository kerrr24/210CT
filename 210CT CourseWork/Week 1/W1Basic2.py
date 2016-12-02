userNum = input("Enter Number: ")
if "." not in userNum:                  #This if statement checks if the user has added decimnals to the number
    print("To Check " + userNum + ".0")
    userNumStr = str(userNum) + ".0"    # and if not adds it to the end for a represtation to show the user what numbr has been checked
    print(userNumStr)
else:
    print("To Check " + userNum)

    userNumStr = str(userNum)
i = 0

pointsUsed = 1
endi = len(userNumStr)           #base case for i count
userNumList = list(userNumStr)
print(userNumList)

while i < endi:
    if userNumList[i] != "0" and userNumList[i] != "." : #if the value of position i of userNumList isn't 0 or . then it adds on to the value of i and carrys on the while loop
        lastNumPos = i  #Sets value of last non 0 number location to the current i as this will be used later to calculate 
        i = i + 1
    elif userNumList[i] == ".":
        pointsUsed = 1   #set number of points used to 1
        i = i + 1
    else:
        i = i + 1
listOfchecknums = ['1','2','3','4','5','6','7','8','9']
if userNumList[i- 2] in listOfchecknums  and userNumList[i-1] == '0': : #check to see if only one 0 at end
    print("Number of trailing 0's is: 1")

else:
    print("Number of trailing 0's is: " + str((endi - 1 - lastNumPos - pointsUsed)))
    #endi (length of list) - lastNumPos (postion value of last non 0 number) - pointsUsed (points used in number) = number of repeating 0's at end of number
