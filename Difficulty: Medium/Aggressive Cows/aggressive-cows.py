class Solution:
    def aggressiveCows(self, arr, k):
        # code here
        arr.sort()
        
        left = 1
        right = arr[-1] - arr[0]
        ans = 0
        
        while left<=right:
            dis = (left + right)//2
            
            
            cows = 1
            last_pos = arr[0]
            
            #check if we can place k cows
            
            for i in range(1, len(arr)):
                if arr[i]-last_pos >=dis:
                    cows +=1
                    last_pos =arr[i]
                    
            if cows >=k:
                ans = dis
                left = dis +1
            else:
                right  = dis-1
        return ans        
            