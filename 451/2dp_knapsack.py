"""
Knapsack problem:

In the knapsack problem we are given a set of n items, where each item i is
specified by a size s i and a value vi . We are also given a size bound S (the size of our knapsack).
The goal is to find the subset of items of maximum total value such that sum of their sizes is at
most S (they all fit into the knapsack)

"""

def dp_knapsack( value, size, S ):
    if len( value ) == 0 or len( size ) == 0:
        return 0 

    dp = [ [ 0 for _ in range( S ) ] for _ in range( len( value ) ) ]

    for i in range( len( value ) ):
        if size[ i ] < S:
            dp[ i ][ size[ i ] ] = value[ i ]
         

    for item in range( 1, len( value ) ):
        for bound in range( S ):
            dp[ item ][ bound ] = max( dp[ item - 1 ][ bound ], 
                                       dp[ item - 1 ][ bound - size[ i ] ] + value[ item ] )
    
    return dp[ -1 ][ -1 ]


