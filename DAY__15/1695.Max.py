from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mySet = set()
        max_total = 0
        total = 0
        left = 0

        for right in range(len(nums)):
            while nums[right] in mySet:
                mySet.remove(nums[left])
                total -= nums[left]
                left += 1
            mySet.add(nums[right])
            total += nums[right]
            max_total = max(max_total, total)

        return max_total


solution = Solution()
result = solution.maximumUniqueSubarray([4, 2, 4, 5, 6])
print(result)
