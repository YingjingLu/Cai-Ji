def max_time( string ):
    """ AA: BB """

    res = ""
    if string[ 0 ] == "?":
        if string[ 1 ] == "?" or int( string[ 1 ] ) <= 3:
            res += "2"
        else:
            res += "1"
    else:
        res += string[ 0 ]

    if string[ 1 ] != "?":
        res += string[ 1 ]
    else:
        if res[ 0 ] == "2":
            res += "3"
        else:
            res += "9"

    res += ":"

    if string[ 3 ] != "?":
        res += string[ 3 ]
    else:
        res += "5"

    if string[ 4 ] != "?":
        res += string[ 4 ]
    else:
        res += "9"

    return res 


print( max_time( "?3:??" ) )
print( max_time( "??:??" ) )
print( max_time( "?1:??" ) )
print( max_time( "?2:??" ) )
print( max_time( "?3:??" ) )
print( max_time( "2?:??" ) )
print( max_time( "0?:??" ) )
print( max_time( "1?:??" ) )
print( max_time( "23:??" ) )
print( max_time( "?3:??" ) )
print( max_time( "?3:5?" ) )
print( max_time( "?3:?8" ) )
print( max_time( "?3:?7" ) )
print( max_time( "?3:4?" ) )
print( max_time( "?3:50" ) )
print( max_time( "?3:49" ) )
