INT_MIN = -2**32


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

Recursively iterate from child to parents,
for each node v there are two states:
    - Take the node 
    - Not take the node

THe max weight thus defined as the max( U( v ), N( v ) ). 
Where U( v ) is the weight of taking the current node
N( v ) is the weight of not taking the current node

If not taking the current node:
    iterate through its children and find the maximum between:
    - taking the child 
    - noe taking the child
Thus N( v ) = sum_{ u in children of v} max( N( u ), U( u ) )

If taking the current node, then we add the current weight to it:
U( v ) = w_v + sum_{u \in children of v} N( u )

"""

def N( v ):
    if v.children is None or len( v.children ) == 0:
        return None 
    else:
        _sum = 0
        for child in v.children:
            if N( child ) is None:
                _sum += U( child )
            else:
                _sum += max( U( child ), N( child ) )
        return _sum 

def U( v ):
    if v.children is None or len( v.children ) == 0:
        return v.weight 
    _sum = v.weight 
    for child in v.children:
        res = N( child )
        if res is not None:
            _sum += res 
    return _sum 


def max_weight_independent_set_on_tree( root ):
    # base case leaf node: return the weight of the current node
    if root is None:
        return 0
    n = N( root )
    u = U( root )
    if n is None:
        return u
    return max( u, n )

"""
Optimal Binary Search Trees
"""

