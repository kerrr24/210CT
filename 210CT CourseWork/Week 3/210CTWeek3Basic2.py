numCheck = input("Enter Number: ")
numberTry = int(numCheck)


def primeCheck(number, divider):

    if number == 1: #check to see if number inputted is 1 and if so prints that it is prime
        print(numCheck + " is a prime number")

    else:
        numRemainder = number%divider #calculates the reminder of two numbers divided

        if divider > 1: #if the divider hasn't reached 1

            if numRemainder == 0: #if reminder is 0 then number being tested cn be fully divided by another number therefore it isn't prime
                print(numCheck + " is not a prime number")


            else:
                dividerNum = divider - 1 #decreases the value of the divider
                primeCheck(numberTry, dividerNum)

        else: #if divider has reached 1 then this means that the number can only be divided by itself and 1, making it prime
            print(numCheck + " is a prime number")

primeCheck(numberTry,numberTry - 1)
