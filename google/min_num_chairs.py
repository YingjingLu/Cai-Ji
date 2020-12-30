def min_chair( S, E ):
    line = []
    for i in S:
        line.append( ( i, 1 ) )
    for i in E:
        line.append( ( i, -1 ) )
    line.sort()
    max_count = 0
    count = 0
    for entry in line:
        count += entry[ 1 ]
        max_count = max( max_count, count )
    return max_count