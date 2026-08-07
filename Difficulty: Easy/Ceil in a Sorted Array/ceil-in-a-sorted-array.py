class Solution:
    def findCeil(self, arr, x):
        low = 0
        high = len(arr) - 1
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2

            if arr[mid] >= x:
                ans = mid
                high = mid - 1      # Search for an earlier occurrence
            else:
                low = mid + 1

        return ans