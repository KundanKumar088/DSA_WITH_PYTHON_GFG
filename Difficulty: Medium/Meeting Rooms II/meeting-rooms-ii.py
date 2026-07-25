class Solution:
    def minMeetingRooms(self, start, end):
        start.sort()
        end.sort()
        
        result = 0
        max_count = 0
        
        i =0
        j = 0
        
        while i<len(start):
            if start[i] < end[j]:
                result +=1
                i +=1
                
            else:
                result -=1
                j +=1
                
            max_count = max(max_count, result)    
        return max_count
        
