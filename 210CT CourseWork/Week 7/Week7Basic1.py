import sys

class adjectcyListGraph:

    def __init__(self,value):

        self.node = value
        self.nodesDict = {'k':['None'],'a':['d','j','c'], 'b':['d','g'], 'c':['h','i'], 'd':['b','a','e'], 'e':['f','d'], 'f':['e','a'], 'g':['h'], 'h':['c','i'], 'i':['c','h'], 'j':['b','e'] }

    def addNode(self, value):

        self.nodesDict.update({value: 'None'}) #When added a new node a value doesn't have to be set, this makes that value NOne which is then altered once the user wants to update the nodes values
        alg.displayList() #runs display function

    def addNeighbour(self,value,Neighbour):
        if 'None' in self.nodesDict[value]: #As None was set as the valkue ealier, this is used to check if it is still in the values

            del self.nodesDict[value] #deletes the None value from the key's values
            self.nodesDict.update({value:Neighbour})#sets a new value for the key to that entered above
            alg.displayList() #runs display function
            
        else: #if None has already been removed/not present then the code belwo runs

            self.nodesDict[value].append(Neighbour) #sets a new value for the key to that entered above
            alg.displayList() #runs display function

    def displayList(self):

        print(self.nodesDict) #prints the node dictionary




alg = adjectcyListGraph(None)
alg.addNode('p')
alg.addNeighbour('p','j')
alg.addNeighbour('a','l')
        
