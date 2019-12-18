
class Binary_Node( object ):

    def __init__( self, weight, left = None, right = None ):
        self.weight = weight 
        self.left = left 
        self.right = right 

class Multi_Node( object ):

    def __init__( self, weight, children ):

        self.weight = weight 
        self.children = children # node list 
        
"""
Max-Weight Indep. Sets on Trees

starting from tree node v the sum of weight of all node is the largest
"""



"""
Optimal Binary Search Trees
"""