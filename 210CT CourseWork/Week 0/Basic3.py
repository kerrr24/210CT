userEnd = "Y"
while userEnd == "Y":
    userX = int(input("Enter X value: "))

    if userX < -2:
        resultX = (userX * userX) + (4 * userX) + 4
        print("f(x) equals " + str(resultX))

    elif userX > -2:
        resultX = (userX * userX) + (5 * userX)
        print("f(x) equals " + str(resultX))

    else:
        print("f(x) equals 0")

    userEnd = input("Start new (Y/N)")
