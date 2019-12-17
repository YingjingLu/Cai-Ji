"""
Strassen's algorithm for matrix multiplication

M (m, k) N ( k, n ) = ( m, n )

function Strassen(M ,N )
if M is 1 × 1 then
return M 11 N 11
end if 
Let M =
A B
C D
and N =
E F
G H

Set S 1 = Strassen(B − D, G + H)
Set S 2 = Strassen(A + D, E + H)
Set S 3 = Strassen(A − C, E + F )
Set S 4 = Strassen(A + B, H)
Set S 5 = Strassen(A, F − H)
Set S 6 = Strassen(D, G − E)
Set S 7 = Strassen(C + D, E)

return = 
S 1 + S 2 − S 4 + S 6, S 4 + S 5
S 6 + S 7, S 2 − S 3 + S 5 − S 7
end function

"""
import numpy as np 


def get_matrix_shape( M ):
    """ 
    Args:
        M <List>
    return the shape of the matrix return it as tuple 

    return None if M is not a valid matrix
    """

    res_shape = []

    m = M 
    while type( m ) == list:
        res_shape.append( len( m ) )
        m = m[ 0 ]
    

    if len( res_shape ) == 0:
        return None 
    return tuple( res_shape  )


def naive_2d( M, N ):
    shape_m = get_matrix_shape( M )
    shape_n = get_matrix_shape( N )

    assert ( shape_m is not None ) and ( shape_n is not None )
    assert len( shape_m ) == 2 and len( shape_n ) == 2
    assert shape_m[ 1 ] == shape_n[ 0 ]

    res = []
    for row_m in range( shape_m[ 0 ] ):
        res_row = [] 
        for col_n in range( shape_n[ 1 ] ):
            _sum = 0
            for i in range( shape_m[ 1 ] ):
                _sum += M[ row_m ][ i ] * N[ i ][ col_n ]
            res_row.append( _sum )
        res.append( res_row )

    assert get_matrix_shape( res ) == ( shape_m[ 0 ], shape_n[ 1 ] )
    return res 

################################################################################

def divide_4_2d( M ):

    row_half = M.shape[ 0 ] // 2
    col_half = M.shape[ 1 ] // 2 

    return M[ : row_half, :col_half ], M[ : row_half, col_half : ], \
           M[ row_half :, : col_half ], M[ row_half :, col_half : ]
        
def strassen_2d_base( M, N ):
    shape_m = M.shape
    shape_n = N.shape 

    res = []
    for row_m in range( shape_m[ 0 ] ):
        res_row = [] 
        for col_n in range( shape_n[ 1 ] ):
            _sum = 0
            for i in range( shape_m[ 1 ] ):
                _sum += M[ row_m ][ i ] * N[ i ][ col_n ]
            res_row.append( _sum )
        res.append( res_row )
    return np.array( res )

def strassen_2d( M, N ):
    """
    Args:
        M <np.array>
        N <np.array>
    """

    shape_m = M.shape 
    shape_n = N.shape 

    if shape_m[ 0 ] == 1 or shape_n[ 1 ] == 1:
        return strassen_2d_base( M, N )

    A, B, C, D = divide_4_2d( M )
    E, F, G, H = divide_4_2d( N )

    S1 = strassen_2d( B - D, G + H )
    S2 = strassen_2d( A + D, E + H )
    S3 = strassen_2d( A - C, E + F )
    S4 = strassen_2d( A + B, H )
    S5 = strassen_2d( A, F - H )
    S6 = strassen_2d( D, G - E )
    S7 = strassen_2d( C + D, E )

    top_left = S1 + S2 - S4 + S6 
    top_right = S4 + S5 
    Bot_left = S6 + S7 
    bot_right = S2 - S3 + S5 - S7 

    top = np.hstack( ( top_left, top_right ) )
    bot = np.hstack( ( Bot_left, bot_right ) )

    return np.vstack( ( top, bot ) ) 