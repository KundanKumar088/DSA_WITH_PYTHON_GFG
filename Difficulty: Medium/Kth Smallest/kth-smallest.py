import heapq
class Solution:
    def kthSmallest(self, arr, k):
        # Code here
        heap = []
        
        for num in arr:
            heapq.heappush(heap,-num)
            
            if len(heap) > k:
                heapq.heappop(heap)
                
        return -heap[0]        
       
