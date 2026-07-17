class Solution:
    def smallestSubWithSum(self, x, arr):
        # Your code goes here 
        n=len(arr)
        min_len = float('inf')
        curr_sum =0
        left = 0
        
        
        for right in range(n):
            curr_sum += arr[right]
            
            while curr_sum>x:
                min_len = min(min_len, right-left+1)
                curr_sum-=arr[left]
                left +=1
                
        if min_len ==float('inf'):
            return 0
        else:
            return min_len
        
        
        
