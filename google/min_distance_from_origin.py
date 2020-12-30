def d( self, x, y ):
        return x **2 + y ** 2
    
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if( len(points ) <= K ):
            return points
        new_pts = []
        for x, y in points:
            new_pts.append( [ self.d( x, y ), x, y ] )
        new_pts.sort( key = lambda x: x[ 0 ] )
        res = []
        cur = 0
        while cur < K:
            res.append( [ new_pts[ cur ][ 1 ], new_pts[ cur ][ 2 ] ] )
            cur += 1
        return res