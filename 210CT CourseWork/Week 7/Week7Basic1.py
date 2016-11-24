class adjectcyListVertex:

    def __init__(self, value):
        self.valLabel = value
        self.connectedEdges = []

    def addNewNeightbour(self,neighbourNode):
        self.connectedEdges[neighbourNode]
        print(str(self.valLabel) + " connects to " + str(self.connectedEdges))
        
class adjectcyListGraph:
    
    def __init__(self):
        self.listOfNodes = []
        self.totalNodes = 0

    def addNewNode(self, value):
        newAddedNode = adjectcyListVertex(value)
        self.listOfNodes[value] = newAddedNode
        print("Node " + str(self.value) + " added to Graph")
        self.totalNodes += 1

    def addNewEdge(self, node1, node2):
        self.listOfNodes[node1].addNewNeightbour[self.listOfNodes[node2]]




    
