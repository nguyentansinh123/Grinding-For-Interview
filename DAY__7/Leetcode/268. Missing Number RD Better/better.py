from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ex_sum = n * (n + 1) // 2
        actualSum = sum(nums)
        return ex_sum - actualSum

solution = Solution()
result = solution.missingNumber([3,0,1])
print(result)