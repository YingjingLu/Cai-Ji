def get_least_freq( string ):
    if len( string ) == 0:
        return 0
    freq_dict = dict()
    for i in string:
        idx = ord( i )
        freq_dict[ idx ] = freq_dict.get( idx, 0 ) + 1
    least = min( freq_dict.keys() )
    return freq_dict[ least ]

def compare_string( A, B ):
    lst1 = A.split( "," )
    lst2 = B.split( "," )
    freq_1 = [ get_least_freq( s ) for s in lst1 ]
    freq_2 = [ get_least_freq( s ) for s in lst2 ]  

    res = []
    if len( lst2 ) == 0:
        return res 
    for tar_freq in freq_2:
        count = 0
        for src_freq in freq_1:
            if src_freq < tar_freq:
                count += 1
        res.append( count )
    return res

A = "abcd aabc bd"
B = "aaa aa"
print( compare_string( A, B ) )