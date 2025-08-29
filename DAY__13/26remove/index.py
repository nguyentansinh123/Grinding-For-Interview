from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0

        for right in range(len(nums)):
            if nums[right] == nums[left]:
                continue
            else:
                left += 1
                nums[left] = nums[right]

        return left + 1


solution = Solution()
print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
