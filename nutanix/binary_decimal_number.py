
def bin_decimal_number( num ):
    _max = 0
    while num > 0:
        dec = num % 10
        _max = max( dec, _max )
        num = num // 10
    return _max