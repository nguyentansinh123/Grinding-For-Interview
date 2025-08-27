from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}

        for i in range(len(nums)):
            mVal = target - nums[i]

            if mVal in hash:
                return [hash[mVal], i]

            hash[nums[i]] = i
        print(hash)

        return []


solution = Solution()
result = solution.twoSum([2, 7, 1, 15], 9)
print(result)
