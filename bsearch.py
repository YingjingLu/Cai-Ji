def bsearch( nums, s, e, target ):
    while s <= e:
        mid = ( s + e ) // 2
        if mid >= len( nums ):
            return -1
        if nums[ mid ] < target:
            s = mid + 1
        elif nums[ mid ] > target:
            e = mid - 1
        else:
            return mid
    return -1

a = [ 1,2,3,4,5,6 ]
print( bsearch( a, 0, len( a ), 6 ) )
print( bsearch( a, 0, len( a ), 4 ) )
print( bsearch( a, 0, len( a ), 1 ) )
print( bsearch( a, 0, len( a ), 3.5 ) )
print( bsearch( a, 0, len( a ), 6.5 ) )