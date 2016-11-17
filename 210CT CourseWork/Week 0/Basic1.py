userEnd = "Y"
while userEnd == "Y":
    safeB = True
    safeD = True
    userA = int(input("Input A:"))
    userB = int(input("Input B:"))
    userC = int(input("Input C:"))
    userD = int(input("Input D:"))
    if str(userB) == "0" or str(userD) == "0":
        print("Cannot divide by zero")
    else:
        aBYb = userA / userB
        cBYd = userC / userB
        print("A divided by B equals " + str(aBYb))
        print("C divided by D equals " + str(cBYd))

    userEnd = input("Start new (Y/N)")

