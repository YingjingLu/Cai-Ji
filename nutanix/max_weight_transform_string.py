def getMaxRec(string, i, n, lookup): 
      
    # Base Case 
    if i >= n: 
        return 0
  
    # If this subproblem is already solved 
    if lookup[i] != -1: 
        return lookup[i] 
  
    # Don't make pair, so 
    # weight gained is 1 
    ans = 1 + getMaxRec(string, i + 1, n, 
                        lookup) 
  
    # If we can make pair 
    if i + 1 < n: 
          
        # If elements are dissimilar 
        if string[i] != string[i + 1]: 
            ans = max(4 + getMaxRec(string, i + 2, 
                                    n, lookup), ans) 
        # if elements are similar so for 
        # making a pair we toggle any of them. 
        # Since toggle cost is 1 so 
        # overall weight gain becomes 3 
        else: 
            ans = max(3 + getMaxRec(string, i + 2, 
                                    n, lookup), ans) 
    # save and return maximum 
    # of above cases 
    lookup[i] = ans 
    return ans 
  
# Initializes lookup table 
# and calls getMaxRec()  
def getMaxWeight(string): 
  
    n = len(string) 
  
    # Create and initialize lookup table 
    lookup = [-1] * (n) 
  
    # Call recursive function 
    return getMaxRec(string, 0, 
                     len(string), lookup) 
  
# Driver Code 
if __name__ == "__main__": 
    string = "AAAAABB"
    print("Maximum weight of a transformation of", 
           string, "is", getMaxWeight(string)) 
  
# This code is contributed by vibhu4agarwal 
https://www.geeksforgeeks.org/maximum-weight-transformation-of-a-given-string/