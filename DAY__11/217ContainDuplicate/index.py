from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for i in range(len(nums)):
            if nums[i] in hash:
                return True
            else:
                hash[nums[i]] = 1

        print(hash)
        return False


solution = Solution()
result = solution.containsDuplicate([1, 2, 3, 1])
print(result)
