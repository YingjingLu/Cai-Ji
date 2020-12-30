def lbs(arr): 
    n = len(arr) 
  
  
    # allocate memory for LIS[] and initialize LIS values as 1 
    # for all indexes 
    lis = [1 for i in range(n+1)] 
  
    # Compute LIS values from left to right 
    for i in range(1 , n): 
        for j in range(0 , i): 
            if ((arr[i] > arr[j]) and (lis[i] < lis[j] +1)): 
                lis[i] = lis[j] + 1
  
    # allocate memory for LDS and initialize LDS values for 
    # all indexes 
    lds = [1 for i in range(n+1)] 
      
    # Compute LDS values from right to left 
    for i in reversed(range(n-1)): #loop from n-2 downto 0 
        for j in reversed(range(i-1 ,n)): #loop from n-1 downto i-1 
            if(arr[i] > arr[j] and lds[i] < lds[j] + 1): 
                lds[i] = lds[j] + 1 
  
  
    # Return the maximum value of (lis[i] + lds[i] - 1) 
    maximum = lis[0] + lds[0] - 1
    for i in range(1 , n): 
        maximum = max((lis[i] + lds[i]-1), maximum) 
      
    return maximum 

https://www.geeksforgeeks.org/longest-bitonic-subsequence-dp-15/