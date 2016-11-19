numCheck = input("Enter Number: ")
numberTry = int(numCheck)


def primeCheck(number, divider):

    if number == 1:
        print(numCheck + " is a prime number")

    else:
        numRemainder = number%divider
        print(numRemainder)

        if divider > 1:

            if numRemainder == 0:
                print(numCheck + " is not a prime number")


            else:
                dividerNum = divider - 1
                primeCheck(numberTry, dividerNum)

        else:
            print(numCheck + " is a prime number")

primeCheck(numberTry,numberTry - 1)
