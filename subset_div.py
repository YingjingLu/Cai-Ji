def subarraysDivByK(A, K):
    _sum = 0
    count = 0
    d = dict()
    for i in range( len( A ) ):
        _sum += A[ i ]
        c = _sum
        if d.get( c % K ) is not None:
            count += d[ c % K ]
        d[ c % K ] = d.get( c % K, 0 ) + 1
        print( d, count, _sum )
    return count

print( subarraysDivByK( [4,5,0,-2,-3,1], 5 ) )