numCheck = input("Enter Number: ")
numberTry = int(numCheck)
dividerNum = numberTry - 1

def primeCheck(number, divider):
    typeCheck = number%divider
    print(typeCheck)

    if typeCheck == 0:
        print(numCheck + " is not a prime number")

    elif divider == 1 or divider == 0:
        print(numCheck + " is a prime number")

    else:
        divider = divider - 1
        primeCheck(number, divider)

primeCheck(numberTry,dividerNum)
    
