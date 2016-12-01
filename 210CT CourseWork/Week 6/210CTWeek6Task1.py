class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        
 
 
       
def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)
 
############################################################################
    #MY CODE#
 
def in_order(tree):

    current = tree #calls in the head node of the tree
    stackOrder = []
    done = False #used to stop while loop fucntion

    while done is False:
        if current != None: #Check to see if current node is present
            stackOrder.append(current) #adds current node to sorted list
            current = current.left #Sets the current node to the previous nodes left node
        else:   #if the previous node doesn't have and children then this code runs
            if(len(stackOrder)>0):  #check to see that stackOrder is populated, this implies that nodes still have to be sorted
               current = stackOrder.pop()   #sets current node to the node that was last to be add to the sorted list 
               print(current.value)  #prints the value of the current node
               current = current.right #sets current node to the previous nodes right node
               
            else:
                done = True #if stackOrder is empty, implies all nodes and values have been printed, ends loop

#############################################################################
 
if __name__ == '__main__':
   
  t=tree_insert(None,6);
  tree_insert(t,10)
  tree_insert(t,5)
  tree_insert(t,2)
  tree_insert(t,3)
  tree_insert(t,4)
  tree_insert(t,11)
  in_order(t)
