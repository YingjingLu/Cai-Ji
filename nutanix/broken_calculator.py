class Solution:
    def recursive( self, x, y, step ):
        if y <= x:
            return step + ( x - y )
        else:
            if y % 2 == 1:
                return self.recursive( x, ( y + 1 ) // 2, step + 2 )
            else:
                return self.recursive( x, y // 2, step + 1 )
    
    def brokenCalc(self, x, y):
        return self.recursive( x, y, 0 )