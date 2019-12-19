"""
Represent graph as 2d adjacency matrix

for n vertex

n x n adjacency matrix with weight, edge has non-negative weights
"""

INT_MAX = 2**31 - 1

"""
Dijkstra’s Algorithm

Given a graph and a source vertex in the graph, 
find shortest paths from source to all vertices in the given graph.

Starting from one of the vertex, and propagate to all the reachable vertex 

In case to find a specific vertex, stop when finding the target node

Does not work when the graph has negative weight
"""
def dijkstras_algorithm( g, src ):
    """
    Args:
        g: n x n adjacency matrix 
        src <int>: index of the src node
    return:
        The weights to reach each vertex
        The previous node to travel to each vertex
    """
    num_node = len( g )
    total_weights = [ INT_MAX for _ in range( num_node ) ]
    total_weights[ src ] = 0
    predecessor = [ None for _ in range( num_node ) ]

    visited = [ False for _ in range( num_node ) ]
    queue = set()
    queue.add( src )
    while len( queue ) != 0:
        # find the q that has the min distance
        cur_node = None 
        cur_dist = INT_MAX 
        for node in queue:
            if cur_node is None:
                cur_node = node 
                cur_dist = total_weights[ node ]
            else:
                if total_weights[ node ] < cur_dist:
                    cur_node = node 
                    cur_dist = total_weights[ node ]
        # propagate the weight sum
        vertex = cur_node 
        queue.remove( cur_node )
        visited[ vertex ] = True 
        cur_weight = total_weights[ vertex ]
        for i in range( num_node ):
            # if there is an edge
            if g[ vertex ][ i ] != 0 and visited[ i ] == False:
                queue.add( i )
                new_weight = cur_weight + g[ vertex ][ i ]
                if new_weight < total_weights[ i ]:
                    predecessor[ i ] = vertex
                    total_weights[ i ] = new_weight
    return total_weights, predecessor

"""
Bellman-Ford algorithm
"""

def bellman_ford( num_vertex, edges, src ):
    """
    Args:
        num_vertex <int>: number of vertex 
        edges <list>: a list of vertex index ( src, target, weight )
        src <int>: the index of the source vertex
    """
    path_weight = [ INT_MAX for _ in range( num_vertex ) ]
    predecrssor = [ None for _ in range( num_vertex ) ]
    path_weight[ src ] = 0

    for _ in range( num_vertex ):
        for src, tar, weight in edges:
            if path_weight[ src ] + weight < path_weight[ tar ]:
                path_weight[ tar ] = path_weight[ src ] + weight 
                predecrssor[ tar ] = src 

    # check for negative loop:
    for src, tar, weight in edges:
        if path_weight[ src ] + weight < path_weight[ tar ]:
            RuntimeError( " negative weight cycle detected " )

    return path_weight, predecrssor

    
"""
All Pair shortest path
"""

"""
Traveling Sales Person
"""