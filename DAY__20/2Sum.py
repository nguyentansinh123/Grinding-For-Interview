from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            minusVal = target - nums[i]
            if nums[i] in hash:
                return [hash[nums[i]], i]
            hash[minusVal] = i
        return []
        
solution = Solution()
result = solution.twoSum([3,4,5,6], 7)
print(result)
