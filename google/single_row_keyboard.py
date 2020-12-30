def calculateTime(self, keyboard, word):
        cur = 0
        pos_dict = dict()
        for i in range( len( keyboard ) ):
            pos_dict[ keyboard[ i ] ] = i
        res = 0
        for c in word:
            dist = abs( cur - pos_dict[ c ] )
            res += dist
            cur = pos_dict[ c ]
        return res