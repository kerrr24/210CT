userNum = input("Enter Number: ")
i = 0
userNumStr = str(userNum)
pointsUsed = 0
endi = len(userNum)
userNumList = list(userNumStr)
print(userNumList)

while i < endi:
    if userNumList[i] != "0" and userNumList[i] != "." :
        lastNumPos = i
        i = i + 1
    elif userNumList[i] == ".":
        pointsUsed = 1
        i = i + 1
    else:
        i = i + 1

print("Number of trailing 0's is: " + str((endi - lastNumPos - pointsUsed)))
        
        




