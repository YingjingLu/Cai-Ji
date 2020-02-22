class Solution:
    def sift_down( self, arr, n, i ):
        largest = i
        l = i * 2 + 1
        r = i * 2 + 2
        
        if l < n and arr[ l ] > arr[ largest ]:
            largest = l
        if r < n and arr[ r ] > arr[ largest ]:
            largest = r
        if largest != i:
            arr[ largest ], arr[ i ] = arr[ i ], arr[ largest ]
            self.sift_down( arr, n, largest )
    
    def sift_up( self, arr, n, i ):
        if i == 0:
            return
        par = ( i - 1 ) // 2
        
        if( arr[ par ] < arr[ i ] ):
            arr[ par ], arr[ i ] = arr[ i ], arr[ par ]
            self.sift_up( arr, n, par )
        
        
    def findKthLargest(self, nums, k):
        heap = []
        start = 0
        n = 0
        for i in range( len( nums ) ):
            if len( heap ) < k:
                heap.insert( -1, -nums[ i ]  )
                self.sift_up( heap, len( heap ), len( heap ) - 1 )
            else:
                if -nums[ i ] <= heap[ 0 ]:
                    heap.insert( -1, -nums[ i ] )
                    self.sift_up( heap, len( heap ), len( heap ) - 1 )
                    a = heap.pop( -1 )
                    heap[ 0 ] = a
                    self.sift_down( heap, len( heap ), 0 )
            print( heap )
                
        return heap[ 0 ] * -1

a = Solution()

print( a.findKthLargest( [ 3,2,1,5,6,4 ], 2 ) )
