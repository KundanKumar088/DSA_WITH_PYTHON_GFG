class Solution:
    def largest(self, arr):
        # code here
        n = len(arr)
        max = arr[0]
        
        for i in range(0,n):
            if arr[i]> max:
                max = arr[i]
                
            
            
        return max    
