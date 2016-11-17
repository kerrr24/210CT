numberUser = input("Enter Parameter: ")
sqaureparameterNum = int(numberUser)
currentNum = sqaureparameterNum

while True:
    if sqaureparameterNum >= (currentNum * currentNum):
        print("The highest perfect square is: " + str(currentNum * currentNum))
        break;

    else:
        currentNum = currentNum - 1
        
