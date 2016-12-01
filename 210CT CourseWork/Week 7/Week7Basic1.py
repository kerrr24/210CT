import sys

class adjectcyListGraph:

    def __init__(self,value):

        self.nodesDict = {'a':['b','f'], 'b':['d','c','e','a'], 'c':['b','j'], 'd':['b','j'], 'e':['b'], 'f':['a','g'], 'g':['h','i','f'], 'h':['g'], 'i':['g'], 'j':['c','d'] }

    def addNode(self, value):
        self.nodesDict.update({value:None}) #When added a new node a value doesn't have to be set, this makes that value NOne which is then altered once the user wants to update the nodes values
        alg.displayList() #runs display function


    def addNeighbour(self,value,Neighbour):
        if None in self.nodesDict[value]: #As None was set as the valkue ealier, this is used to check if it is still in the values
            del self.nodesDict[value] #deletes the None value from the key's values
            self.nodesDict.update({value:Neighbour}) )#sets a new value for the key to that entered above
            alg.displayList() #runs display function

        else: #if None has already been removed/not present then the code belwo runs
            self.nodesDict[value].append(Neighbour) #sets a new value for the key to that entered above
            alg.displayList() #runs display function


    def displayList(self):
        print(self.nodesDict) #prints the node dictionary


    def BreadthFirst(self, graph, nodesList, currentNode, visited,done):
        queueList = nodesList #creates a queue equal to that of nodesList
        visitedNodes = visited #sets the list of visitedNodes to an updated version
        unvisitedNodes = sorted(list(self.nodesDict.keys())) #creates a lst of all the nodes in alphabetical order
        print(unvisitedNodes)
        tempNodeList = []
        count = 0
        queueList.append(currentNode) #adds the currentNode to the queueList
        while queueList != []: #check to see if queue list is empty, if not run the following code
            previousNode = queueList.pop(0) #gets and removes the element from positon 0 from the list
            if previousNode not in visitedNodes: #check to see if node is already been visited  
                visitedNodes.append(previousNode) #if not adds node to visited
                queueList = queueList + (sorted(self.nodesDict[previousNode])) #adds a sorted list of nodes to the queue
                alg.BreadthFirst(alg.nodesDict, queueList, previousNode, visitedNodes,done)
        return(visitedNodes)


    def depthFirst(self, graph, nodesList, currentNode, visited,done):
        stackList = nodesList #creates a stack equal to that of nodeList
        visitedNodes = visited ##sets the list of visitedNodes to an updated version
        stackList.append(currentNode) #adds the currentNode to the stack
        while stackList != []: #check to see if stack is empty
            previousNode = stackList.pop() #gets and removs element form last postion of the stack
            if previousNode not in visitedNodes: #check to see if node is already been visited 
                visitedNodes.append(previousNode) #if not adds node to visited
                tempList = sorted(self.nodesDict[previousNode])#sorts list of nodes into alphabetical order
                tempList = tempList[::-1] #reverses the order of the list
                stackList = stackList + tempList  #adds a sorted list of nodes to the stack
                alg.depthFirst(alg.nodesDict, stackList, previousNode, visitedNodes,done)

        return(visitedNodes)
         
def writeFile(fileName, toSave):

    textFileName = fileName #filename is given when called from outside function
    stringToSave = str(toSave) #data to save is given when called from outside function

    try:
        textfile = open(textFileName, "a") #opens file for writing, but also creates the file if not already existent
        textfile.write(stringToSave) #writes choosen data to file
        textfile.writelines("\n") #moves to next line in text file
        textfile.close() #closes the file, this saves the changes

    except:
        print("File Creation Went Wrong")        


alg = adjectcyListGraph(None)
DFReturn = alg.depthFirst(alg.nodesDict,[],'a',[],False)
print("Depth First: " + str(DFReturn))
writeFile("depthFirstvisitedNodes.txt", DFReturn)
BFReturn = alg.BreadthFirst(alg.nodesDict,[],'a',[],False)
print("Breadth First: " + str(BFReturn))
writeFile("BreadthFirstvisitedNodes.txt",BFReturn)
