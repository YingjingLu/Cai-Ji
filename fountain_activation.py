def fountain_activation( lst ):
    n = len( lst )
    if n == 0:
        return n
    right_most = [ 0 for _ in range( n ) ]
    for i in range( n ):
        right_most[ max( 0, i - lst[ i ]  ) ] = min( n, i + lst[ i ] )
    l, r, count = 0, right_mist[ 0 ], 0
    while r <= n:
        new_r = r
        count += 1
        while l <= r:
            new_r = max( right_most[ l ], new_r )
            l += 1
        if l >= n:
            break
        r = max( new_r, right_most[ l ] )
    return count
