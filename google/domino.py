def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        a_has = { k:0 for k in range( 1, 7 ) }
        b_has = { k:0 for k in range( 1, 7 ) }
        a_comp = { k:0 for k in range( 1, 7 ) }
        b_comp = { k:0 for k in range( 1, 7 ) }
        
        for i in range( len( A ) ):
            a = A[ i ]
            b = B[ i ]
            a_has[ a ] = a_has.get( a, 0 ) + 1
            b_has[ b ] = b_has.get( b, 0 ) + 1
            if a != b:
                a_comp[ b ] = a_comp.get( b, 0 ) + 1
                b_comp[ a ] = b_comp.get( a, 0 ) + 1
        min_step = 2**31 - 1
        for i in range( 1, 7 ):
            
            if a_has[ i ] + a_comp[ i ] == len( A ):
                min_step = min( min_step, a_comp[ i ] )
            if b_has[ i ] + b_comp[ i ] == len( B ):
                min_step = min( min_step, b_comp[ i ] )
        if min_step == 2**31 - 1:
            return -1
        return min_step