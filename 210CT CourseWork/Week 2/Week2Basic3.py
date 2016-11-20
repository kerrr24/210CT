Matrix1 <- UserInput
Matrix2 <- UserInput
MatrixBase <- Matrix of all 0's

MATRIXADDITION(Matrix1, Matrix2, done)

    currentX <- 0
    currentY <- 0
    matrixXMax <- len(Matrix1[0]) - 1
    matrixYMax <- len(Matrix1) - 1
    addMatrixResult <- MatrixBase

    while done = True

        if currentY <= matrixYMax

            if currentX <= matrixXMax
                addMatrixResult[currentY,currentX] <- Matrix1[currentY,currentX] + Matrix2[currentY,currentX]
                currentX <- currentX + 1

            else
                currentX <- 0
                currentY <- currentY + 1
        else
            print addMatrixResult
            return addMatrixResult  


MATRIXSUBSTRACTION(Matrix1, Matrix2)

    currentX <- 0
    currentY <- 0
    matrixXMax <- len(Matrix1[0]) - 1
    matrixYMax <- len(Matrix1) - 1
    subMatrixResult <- MatrixBase

    while done = True

        if currentY <= matrixYMax

            if currentX <= matrixXMax
                subMatrixResult[currentY,currentX] <- Matrix1[currentY,currentX] - Matrix2[currentY,currentX]
                currentX <- currentX + 1

            else
                currentX <- 0
                currentY <- currentY + 1
        else
            print subMatrixResult
            return subMatrixResult 


MATRXIMULTIPLCATION(Matrix1, Matrix2)

    multiMatrixResult <- filled matrix of all 0
    currentX <- 0
    yCount <- 0
    xCount <- 0
    currentY <- 0
    matrixXMax <- len(Matrix1[0]) - 1
    matrixYMax <- len(Matrix1) - 1
    MultiMatrixResult <- MatrixBase

    while done = False

        if currentY <= matrixYMax

            if currentX <= matrixXMax

                while xCount <= matrixXMax

                    multiMatrixResult[currentY][currentX] <- multiMatrixResult[currentX][currentY] + ( Matrix1[currentY][xCount] * Matrix2[yCount][currentX] ) 
                    xCount <- xCount + 1
                    yCount <- yCount + 1

                currentX <- currentX + 1
                xCount <- 0
                yCount <- 0
                
            else
            
                currentX <- 0
                currentY <- currentY + 1
                MATRXIMULTIPLCATION(Matrix1, Matrix2,currentX,currentY)
                
        else
            done <- True
            print MultiMatrixResult
            return multiMatrixResult
