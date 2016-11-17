eggsPerDay = input("Number of eggs laid per day: ")
numberOfDays = input("Number of days till egss hatch: ")
lengthOfInvasion = input("Length of the invasion last: ")
numberOfStartAlien = input("How many starting aliens: ")
AlienAmountList = []
AlienAmountList.append(int(numberOfStartAlien))
currentDay = 0
addCount = 1

while addCount < int(lengthOfInvasion):
    AlienAmountList.append(0)
    addCount = addCount + 1
print(AlienAmountList)


while currentDay < int(lengthOfInvasion):
    k = currentDay + int(numberOfDays)

    if currentDay >= (int(lengthOfInvasion) - int(numberOfDays) ):
        AlienAmountList[currentDay] = AlienAmountList[currentDay] + AlienAmountList[currentDay - 1]
        currentDay = currentDay + 1
        
    else:
        AlienAmountList[currentDay] = AlienAmountList[currentDay] + AlienAmountList[currentDay - 1]
        newEggs = AlienAmountList[currentDay] * int(eggsPerDay)
        print(newEggs)
        AlienAmountList.pop(k)
        AlienAmountList.insert(k , newEggs)
        currentDay = currentDay + 1

lastAliens = int(lengthOfInvasion) - 1
print(AlienAmountList)
print("There will be " + str(AlienAmountList[lastAliens]) + " Alien(s) after " + lengthOfInvasion + " days")
        
    

