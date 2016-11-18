numberUser = input("Enter Parameter: ")
checkDone = False
sqaureparameterNum = int(numberUser)
currentNum = sqaureparameterNum

while checkDone == False:
    if sqaureparameterNum >= (currentNum * currentNum):
        print("The highest perfect square is: " + str(currentNum * currentNum))
        checkDone = True

    else:
        currentNum = currentNum - 1
        
