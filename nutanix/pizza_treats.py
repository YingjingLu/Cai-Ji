
def pizza_treats( arr ):
    prev = 0
    for i in arr:
        if i - prev < 0:
            return "NO"
        else:
            if ( i - prev ) % 2 == 0:
                prev = 0
            else:
                prev = 1
    if prev == 0:
        return "YES"
    return "NO"

print( pizza_treats( [ 1,2,1,2 ] ) )
print( pizza_treats( [ 1, 0, 1 ] ) )