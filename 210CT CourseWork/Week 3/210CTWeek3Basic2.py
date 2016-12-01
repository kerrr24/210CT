numCheck = input("Enter Number: ")
numberTry = int(numCheck)
dividerNum = numberTry - 1 #sets diver to ojne less than the number being tested

def primeCheck(number, divider):

    if number == 1:
        print(numCheck + " is a prime number")
    else:
        divNumCheck = number%divider #finds remeinder of number
        #print(divNumCheck)

    if divNumCheck == 0 and divider != 1: #if no reminder than number isnt prime
        print(numCheck + " is not a prime number")

    elif divider == 1 or divider == 0: #if divider gets to 1 (0 for number = 1) then number is prime
        print(numCheck + " is a prime number")


    else:
        divider = divider - 1
        print(divider)
        primeCheck(number, divider) #recursive call of function with updated values to be used

primeCheck(numberTry,dividerNum)
