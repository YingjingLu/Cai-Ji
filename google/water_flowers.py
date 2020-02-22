
def water_flower( plants, capacity1, capacity2 ):

    count = len( plants )
    refill = 0
    # no plants to water
    if count == 0:
        return refill
    # calculate number of flowers left and rght has to water
    # and starting index for left and right person
    if count % 2 == 0:
        left_num = right_num = count // 2
    else:
        left_num = right_num = ( count - 1 ) // 2
    left_cur_idx = 0 # left person always start from the first
    right_cur_idx = count - 1 # right person starts fromt the other end
    # keep track of both person's remaining water, starting 0
    left_remain = right_remain = 0
    # simulate left
    while left_num > 0:
        # if not enough water, refill
        if plants[ left_cur_idx ] > left_remain:
            left_remain = capacity1
            refill += 1
        left_remain -= plants[ left_cur_idx ]
        left_cur_idx += 1
        left_num -= 1
    # simulate right in the same fashion as in left
    while right_num > 0:
        if plants[ right_cur_idx ] > right_remain:
            right_remain = capacity2
            refill += 1
        right_remain -= plants[ right_cur_idx ]
        right_cur_idx -= 1
        right_num -= 1
    # in case fill the middle one
    if count % 2 == 1:
        mid = plants[ count // 2 ]
        # in case not enough water 
        if right_remain + left_remain < mid:
            if capacity1 + right_remain > mid or capacity2 + left_remain > mid:
                refill += 1
            else:
                refill += 2

    return refill


print( water_flower( [ 2,5,7 ], 5, 7 ) )