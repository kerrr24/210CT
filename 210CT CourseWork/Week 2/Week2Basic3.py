import copy #imports the ability to copy values


Matrix1 = [[2, 2, 2,], [1, 2, 2,], [1, 2, 2,]]
Matrix2 = [[1, 2, 2,], [2, 2, 2,], [1, 2, 2,]]
MatrixBase =  [0, 0, 0,], [0, 0, 0,], [0, 0, 0,]
done = False
done2 = False


def MATRIXADDITION(Matrix1, Matrix2, done): #Following code is used to add two matrices together 

    currentX = 0
    currentY = 0
    matrixXMax = len(Matrix1[0]) - 1
    matrixYMax = len(Matrix1) - 1
    addMatrixResult = MatrixBase
    addDone = done
    

    while addDone == False:

        if currentY <= matrixYMax: #checks to see if the y value is within it's set limits otherwise this code doesn't run
            
            if currentX <= matrixXMax:
                addMatrixResult[currentY][currentX] = Matrix1[currentY][currentX] + Matrix2[currentY][currentX] #adds together the matrices one by one for example if location (0,0) in matrix1 was 2 and (0,0) in matrix2 was 5 the answer would be 7
                currentX = currentX + 1 #moves across a coloum

            else:
                currentX = 0
                currentY = currentY + 1 #moves down a row

        else:
            addDone = True

    if addDone == True:
        return addMatrixResult
        
    

def MATRIXSUBTRACTION(MatrixSub1, MatrixSub2, done, result): #Following code is used to subtract two matrices

    currentX = 0
    currentY = 0
    matrixXMax = len(MatrixSub1[0]) - 1
    matrixYMax = len(MatrixSub1) - 1
    subMatrixResult = MatrixBase
    done = False

    while done == False:

        if currentY <= matrixYMax:
            
            if currentX <= matrixXMax: #checks to see if the y value is within it's set limits otherwise this code doesn't run
                subMatrixResult[currentY][currentX] = MatrixSub1[currentY][currentX] - MatrixSub2[currentY][currentX] #subtracts the matrices one by one for example if location (0,0) in matrix1 was 2 and (0,0) in matrix2 was 5 the answer would be -3
                #print(addMatrixResult)
                currentX = currentX + 1 #moves across a coloum

            else:
                currentX = 0
                currentY = currentY + 1 #moves down a row

        else:
            done = True

    return subMatrixResult



def MATRXIMULTIPLCATION(Matrix1Multi, Matrix2Multi,curX,curY): #Following code is used to multiply two matrices together

    intCheck = isinstance( Matrix1Multi, int ) #checks if matrix1 is an intger
    currentX = curX
    yCount = 0
    xCount = 0
    currentY = curY
    matrixXMax = len(Matrix2Multi[0]) - 1
    matrixYMax = len(Matrix2Multi) - 1
    global done
    MultiMatrixResult = MatrixBase
    MultiMatrixResult2 = MatrixBase

    while done == False:

            if currentY <= matrixYMax: #checks to see if y is smaller or equal to its set max boundaries
                
                

                if currentX <= matrixXMax: #checks to see if x is smaller than its max boundaries


                    while xCount <= matrixXMax: #runs while the xcount is less than the max x

                        tempMulti = Matrix1Multi[currentY][xCount] * Matrix2Multi[yCount][currentX] #multiplies matrix 1 against matrix 2, coloums and rows vary
                        MultiMatrixResult[currentY][currentX] +=  tempMulti 
                        xCount = xCount + 1 #moves the x value of matrix 1 right one
                        yCount = yCount + 1 #moves the y value of matrix 2 down one
                        
                    currentX = currentX + 1 #sets the current x location to one to the right
                    xCount = 0
                    yCount = 0
                    
                else:

                    currentX = 0
                    currentY = currentY + 1 #moves down a row
                    MATRXIMULTIPLCATION(Matrix1Multi, Matrix2Multi,currentX,currentY) #recursive call of function to run again but with different x and y values


            else:
                done = True

            

    if done == True:
        return MultiMatrixResult

def MATRIXMULTIWHOLENUM(Matrix1Multi, Matrix2Multi,curX,curY): #Following code is used to multiply a matrix by an interger

        MultiMatrixResult2 = MatrixBase
        currentX = curX
        currentY = curY
        matrixXMax = len(Matrix2Multi[0]) - 1
        matrixYMax = len(Matrix2Multi) - 1
        global done2
        global multiBaddC
        
        while done2 == False:

            if currentY <= matrixYMax: #checks to see if y is within it max boundaires
            
                if currentX <= matrixXMax: #checks to see if x is within it max boundaires
                    
                    
                    while currentX <= matrixXMax:



                        tempMulti = Matrix2Multi[currentY][currentX] * Matrix1Multi #multiples matrix 2 by Matrix1Multi, for example if matrix 2 (0,0) was 2 and Matrix1Multi was 4 the answer would be 8
                        MultiMatrixResult2[currentY][currentX] =  tempMulti 
                        
                        currentX = currentX + 1 #moves across a coloum

                    
                else:

                    currentX = 0
                    currentY += 1 #moves down a row
                    MATRIXMULTIWHOLENUM(Matrix1Multi, Matrix2Multi,currentX,currentY)


            else:
                done2 = True
                
        if done2 == True:
            multiBaddC = MultiMatrixResult2
            return MultiMatrixResult2



def resultCalculation():
    BMultiC = copy.deepcopy(MATRXIMULTIPLCATION(Matrix1, Matrix2,0,0)) #copys list and the objects in it
    print("B*C = "+str(BMultiC))
    BaddC = copy.deepcopy(MATRIXADDITION(Matrix1, Matrix2,False)) #copys list and the objects in it
    print("B+C = "+str(BaddC))
    multiBaddC = copy.deepcopy(MATRIXMULTIWHOLENUM(2, BaddC,0,0)) #copys list and the objects in it
    print("2(B+C) = "+str(multiBaddC))
    endResult = MATRIXSUBTRACTION(BMultiC, multiBaddC, False, True)
    print("B*C - 2(B+C) = " + str(endResult))



                      
resultCalculation()
