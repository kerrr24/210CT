Matrix1 <- UserInput
Matrix2 <- UserInput

MATRIXADDITION(Matrix1, Matrix2)

currentX <- 0
currentY <- 0

while True

    if currentX <= matrixXMax
        addMatrixResult(currentX,currentY) <- Matrix1(currentX,currentY) - Matrix2(currentX,currentY)
        currentX <- currentX + 1

    else
        currentX <- 0
        currentY <- currentY + 1
        
        if currentY > matrixYMax
            break

print addMatrixResult


MATRIXSUBSTRACTION(Matrix1, Matrix2)

currentX <- 0
currentY <- 0

while True

    if currentX <= matrixXMax
        subMatrixResult(currentX,currentY) <- Matrix1(currentX,currentY) + Matrix2(currentX,currentY)
        currentX <- currentX + 1

    else
        currentX <- 0
        currentY <- currentY + 1
        
        if currentY > matrixYMax
            break

print subMatrixResult


MATRXIMULTIPLCATION(Matrix1, Matrix2)

multiMatrixResult <- filled matrix of all 0
currentX <- 0
yCount <- 0
xCount <- 0
currentY <- 0

while True

    if currentX <= matrixXMax

        for xCount <= matrixXMax

            multiMatrixResult(currentX,currentY) <- multiMatrixResult(currentX,currentY) + (  Matrix1(xCount,currentY) * Matrix2(currentX,yCount) ) 
            xCount <- xCount + 1
            yCount <- yCount + 1

        currentX <- currentX + 1
        
    else
    
        currentX <- 0
        currentY <- currentY + 1
        
        if currentY > matrixYMax
            break
        
print multiMatrixResult

        














    
