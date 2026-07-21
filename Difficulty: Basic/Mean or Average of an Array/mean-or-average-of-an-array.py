class Solution:
    def findMean(self, arr):
        # code here 
        n = len(arr)
        sum = 0
        
        for i in range(n):
            
            sum = sum +arr[i]
            
        return sum//n    