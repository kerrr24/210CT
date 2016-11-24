
userList = input("Enter values with spaces between: ")
userList = userList.split()
findelem = input("Number to check for: ")


def binarySearch(array, point):
    def repeat(first, last):
        midPoint = (len(array)) / 2
        if point == array[midPoint]:
            return midPoint
        elif point > midPoint:
            return repeat(midPoint + 1, last)
        elif point < midPoint:
            return repeat(first, last - 1)

    return repeat(0, len(userList)-1)

binarySearch(userList, findelem)
