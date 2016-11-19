import random

listStr = input("Enter list of numbers with single space between numbers: ")
numList = listStr.split()
listLeng = len(numList)
print("Starting list was: " + str(numList))

currentY = 0

while currentY < listLeng:               #Following code runs while currentY is less than the length of the list
    x = random.randint(0,(listLeng - 1)) #sets x, a temp value, to a random number between 0 and 1 less than the length of the list
    currentNum = numList[currentY]       #sets currentNum to the same value as postion currentY in list numList
    swapNum = numList[x]                 #sets swapNum to the same value as postion x in list numList
    numList[currentY] = swapNum          #Following two lines swap numList[currentY] with numList[x]
    numList[x] = currentNum
    currentY = currentY + 1

print("Randomised list is now: " + str(numList))
