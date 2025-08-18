
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        res = 0

        while right > left:
            amount = (right - left) * min(height[right], height[left])
            res = max(res, amount)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return res
        
        

solution = Solution()
result = solution.maxArea([1,8,6,2,5,4,8,3,7])
print(result)