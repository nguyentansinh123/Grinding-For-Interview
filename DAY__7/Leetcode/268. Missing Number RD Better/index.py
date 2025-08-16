from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new_nums = sorted(nums)        
        for i in range(new_nums[-1]):
            if i not in nums:
                return i
        return new_nums[-1] + 1



solution = Solution()
result = solution.missingNumber([3,0,1])
print(result)