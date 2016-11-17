divCheck <- False
newDictionary <- valSplitDict

While divCheck = False
    For valCount <- 2 to 12
        If userVal div valCount
            valSplit1 <- valCount
            userVal <- userVal/valCount
            
            If valSplit1 In valSplitDict
                valSplitDict[valSplit1][0] <- valSplitDict[valSplit1][0] + 1
            valCount <- 2
        Else If valCount = 12
            divCheck <- True     
        Else
            valCount <- (valCount + 1)

For valCount <- 0 to length[valSplitDict]
    If valSplitDict[valCount][0] > valSplitDict[valCount + 1][0]
        valSplitDict[valCount + 1][0] <- valSplitDict[valCount][0]
        valCount <- valCount + 1
    Else
        valCount <- valCount + 1


        
        
