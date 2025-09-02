from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSum = 0

        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSub = max(maxSub, currSum)
        return maxSub


solution = Solution()
result = solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(result)
