userEnd = "Y"
while userEnd == "Y":
    print("Enter Following Data in Nunmber form")
    userDay = input("Day: ")
    userMonth = input("Month: ")
    userYear = input("Year: ")

    if int(userMonth) <= 12 and int(userDay) >= 1 and int(userDay) <= 31 :
        
        if (int(userYear)% 4) == 0 and (int(userYear) % 100 != 0 or int(userYear) % 400 == 0) == 0:
            numOfDays = 366
            lenFeb = 30
            lenMon = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        else:
            numOfDays = 365
            lenFeb = 29
            lenMon = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

        countMon = 1

        while countMon <= int(userMonth):
            numOfDays = numOfDays - lenMon[countMon]
            if countMon == int(userMonth):
                break;
            else:
                countMon = countMon + 1

        daysLeftMOn = lenMon[countMon] - int(userDay)
        numOfDays = numOfDays + daysLeftMOn

        print( str(12 - (countMon+1)) + " Full Months left  With " + str(daysLeftMOn) + " Days left within the current month")
        print("Total Days Left: " + str(numOfDays))
        userEnd = input("Start new (Y/N) ")
    else:
        print("Invalid Day")

