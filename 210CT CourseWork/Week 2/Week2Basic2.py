TASK 1

import random

listStr = input("Enter list of numbers with single space between numbers: ")      1
numList = listStr.split()                       1
listLeng = len(numList)                         1
print("Starting list was: " + str(numList))     1

currentY = 0                                    1

while currentY < listLeng:                      n    
    x = random.randint(0,(listLeng - 1))        n
    currentNum = numList[currentY]              n
    swapNum = numList[x]                        n
    numList[currentY] = swapNum                 n
    numList[x] = currentNum                     n
    currentY = currentY + 1                     n

print("Randomised list is now: " + str(numList))        1

= 7n + 6
= O(n)


TASK 2

userNum = input("Enter Number: ")                                   1
if "." not in userNum:                                              1
    print("To Check " + userNum + ".0")                             1
else:                                                               1
    print("To Check " + userNum)                                    1
i = 0                                                               1
userNumStr = str(userNum)                                           1
pointsUsed = 0                                                      1
endi = len(userNum)                                                 1
userNumList = list(userNumStr)                                      1
print(userNumList)                                                  1

while i < endi:                                                     n+1
    if userNumList[i] != "0" and userNumList[i] != "." :            n
        lastNumPos = i                                              n
        i = i + 1                                                   n
    elif userNumList[i] == ".":                                     n
        pointsUsed = 1                                              n
        i = i + 1                                                   n
    else:                                                           n
        i = i + 1                                                   n

print("Number of trailing 0's is: " + str((endi - lastNumPos - pointsUsed)))        1


= 9n + 13
= O(n)



