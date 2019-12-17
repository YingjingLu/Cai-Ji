"""
The LCS problem:
The Longest Common Subsequence (LCS) problem is as follows. We are given
two strings: string S of length n, and string T of length m. Our goal is to produce their longest
common subsequence: the longest sequence of characters that appear left-to-right (but not necessarily
in a contiguous block) in both strings.

"""
def longest_common_subsequence( s, t ):
    if len( s ) == 0 or len( t ) == 0:
        return 0

    dp = [ [ 0 for i in range( len( t ) ) ] for _ in range( len( s ) ) ] 

    # base case
    for i in range( len( t ) ):
        if t[ i ] == s[ 0 ]:
            dp[ 0 ][ i ] = 1
    
    for i in range( len( s ) ):
        if s[ i ] == t[ 0 ]:
            dp[ i ][ 0 ] = 1

    # recursive case 
    for row in range( 1, len( s ) ):
        for col in range( 1, len( t ) ):
            if s[ row ] == t[ col ]:
                dp[ row ][ col ] = dp[ row - 1 ][ col - 1 ] + 1
            else:
                dp[ row ][ col ] = dp[ row - 1 ][ col - 1 ]
    return dp[ -1 ][ -1 ]

def longest_common_consecutive_subsequence( s, t ):
    """
    common subsequence that has to be consecutive
    """

    if len( s ) == 0 or len( t ) == 0:
        return 0

    dp = [ [ 0 for i in range( len( t ) ) ] for _ in range( len( s ) ) ] 

    # base case
    for i in range( len( t ) ):
        if t[ i ] == s[ 0 ]:
            dp[ 0 ][ i ] = 1
    
    for i in range( len( s ) ):
        if s[ i ] == t[ 0 ]:
            dp[ i ][ 0 ] = 1
    _max = 0

    # recursive case 
    for row in range( 1, len( s ) ):
        for col in range( 1, len( t ) ):
            if s[ row ] == t[ col ]:
                dp[ row ][ col ] = dp[ row - 1 ][ col - 1 ] + 1
            else:
                dp[ row ][ col ] = 0
            
            _max = max( _max, dp[ row ][ col ] )
    return _max 

def longest_common_subset( s, t ):
    """
    count common elems ignoring order
    """
    
    s_dict = dict()
    t_dict = dict()

    for elem in s:
        s_dict[ elem ] = s_dict.get( elem, 0 ) + 1
    for elem in t:
        t_dict[ elem ] = t_dict.get( elem, 0 ) + 1
    
    common = 0
    for elem in s_dict:
        if elem in t_dict:
            common += min( s_dict[ elem ], t_dict[ elem ] )
    return common