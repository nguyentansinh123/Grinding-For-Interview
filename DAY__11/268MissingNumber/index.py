from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = max(nums)
        for i in range(res):
            if i not in nums:
                return i
        return res + 1


solution = Solution()
result = solution.missingNumber([3, 0, 1])
print(result)
