def max_sub( arr, k ):
    if len( arr ) <= k:
        return arr 
    elif k <= 0:
        return []

    cur_start = 0
    cur_end = k
    max_start = 0
    max_end = k

    max_sum = sum( arr[ cur_start: cur_end ] )
    cur_sum = max_sum
    while cur_end < len( arr ):
        cur_sum -= arr[ cur_start ]
        cur_sum -= arr[ cur_end -1 ]
        cur_start += 1
        cur_end += 1
        cur_sum += arr[ cur_start ]
        cur_sum += arr[ cur_end -1 ]
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_start = cur_start
            max_end = cur_end 
    return arr[ max_start: max_end ]

arr = [ 1,4,3,2,5 ]
k  = 4
print( arr, k, max_sub( arr, k ) )

arr = [ 1,4,3,2,5 ]
k  = 0
print( arr, k, max_sub( arr, k ) )

arr = [ 1,4,3, ]
k  = 4
print( arr, k, max_sub( arr, k ) )

arr = [ 1,4,3,2,5, 7 ]
k  = 2
print( arr, k, max_sub( arr, k ) )

arr = [ 1,4,3,2,5 ]
k  = 1
print( arr, k, max_sub( arr, k ) )

arr = [ 1,4,3,2,5, 8, 9 ]
k  = 3
print( arr, k, max_sub( arr, k ) )

arr = [ 1,4,3,0,5 ]
k  = 4
print( arr, k, max_sub( arr, k ) )

arr = [ 1,4,8,2,5 ]
k  = 3
print( arr, k, max_sub( arr, k ) )

arr = [ 1,4,3,2,5 ]
k  = 2
print( arr, k, max_sub( arr, k ) )

arr = [ 9,4,3,2,5 ]
k  = 2
print( arr, k, max_sub( arr, k ) )

arr = [ 9,4,9,9,5 ]
k  = 2
print( arr, k, max_sub( arr, k ) )
