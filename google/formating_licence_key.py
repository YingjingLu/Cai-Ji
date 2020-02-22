def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        raw_str = S.split( "-" )
        raw_str = ( "".join( raw_str ) ).upper()
        new_lst = []
        if len( raw_str ) <= K:
            return raw_str
            
        cur_start = len( raw_str ) - K
        while cur_start >= 0:
            new_lst.insert( 0, raw_str[ cur_start: cur_start + K ] )
            cur_start -= K
        if cur_start + K > 0:
            new_lst.insert( 0, raw_str[ 0: cur_start + K ] )
        return "-".join( new_lst )