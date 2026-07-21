class Solution:
    def getSecondLargest(self, arr):
        # code here
        n = len(arr)
        
        max = arr[0]
        secmax = -1
        
        for i in range (0,n):
            if arr[i]>max:
                max = arr[i]
            
        for i in range(0,n):
            if arr[i]>secmax and arr[i]!= max:
                secmax = arr[i]
            
                
                
        return secmax       
                
            