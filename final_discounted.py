def final_price( prices ):
    res = []
    if not prices:
        return res 
    stack = []
    for i in range( len( prices ) - 1, -1, -1 ):
        if len( stack ) == 0:
            stack.append( prices[ i ] )
            res.insert( 0, prices[ i ] )
            continue
        while( len( stack ) != 0 and stack[ -1 ] > prices[ i ] ):
            stack.pop()
        if len( stack ) == 0:
            res.insert( 0, prices[ i ] )
        else:
            res.insert( 0, prices[ i ] - stack[ -1 ] )
        stack.append( prices[ i ] )

    return res 
print( final_price( [ 2,3,1,2,4,2 ] ) )
