class Solution:
    def isIntersect(self, intervals):
        
       # Code Here
        n = len(intervals)
    
       
        intervals.sort(key=lambda x: x[0])
        
         
        # intersects with its previous
        for i in range(1, n):
            if intervals[i][0] <= intervals[i - 1][1]:
                return True
        return False    
           
       