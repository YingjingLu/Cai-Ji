class Solution:
    def canCross1(self, stones: List[int]) -> bool:
        if( len( stones ) < 2 or stones[ 1 ] - stones[ 0 ] != 1 ):
            return False
        # depth first search
        stack = [] # pos_idx, step
        cur_idx = 1
        stack.append( [ 1, 1 ] )
        while( len( stack) > 0 and stack[ -1 ][ 0 ] != len( stones ) - 1 ):
            idx, step = stack.pop( -1 )
            for i in range( idx + 1, len(  stones ) ):
                new_step = abs( stones[ i ] - stones[ idx ] )
                if abs( new_step - step ) <= 1:
                    stack.append( [ i, new_step ] )
        if len( stack ) == 0:
            return False
        return True
    
    def canCross(self, stones: List[int]) -> bool:
        if( len( stones ) < 2 or stones[ 1 ] - stones[ 0 ] != 1 ):
            return False
        d = dict()
        for i in range( len( stones ) ):
            d[ stones[ i ] ] = set()
            
        d[ 0 ].add( 0 )
        for i in range( len( stones ) ):
            for j in d[ stones[ i ] ]:
                for step in range( j - 1, j + 2 ):
                    if step > 0 and d.get( stones[ i ] + step ) is not None:
                        d[ stones[ i ] + step ].add( step )
        return len( d [ stones[ -1 ] ] ) > 0