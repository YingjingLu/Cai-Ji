
def paint_fence( arr ):
    pos = []
    for i in range( len( arr ) ):
        if arr[ i ] == 1:
            pos.append( i )
    if len( pos ) == 0:
        return 0
    total = 1

    for i in range( 1, len( pos ) ):
        total *= pos[ i ] - pos[ i-1 ]
    return total
    
