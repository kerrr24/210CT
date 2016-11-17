import random

listStr = input("Enter list of numbers with single space between numbers: ")
numList = listStr.split()
listLeng = len(numList)
print("Starting list was: " + str(numList))

currentY = 0

while currentY < listLeng:
    x = random.randint(0,(listLeng - 1))
    currentNum = numList[currentY]
    swapNum = numList[x]
    numList[currentY] = swapNum
    numList[x] = currentNum
    currentY = currentY + 1

print("Randomised list is now: " + str(numList))
