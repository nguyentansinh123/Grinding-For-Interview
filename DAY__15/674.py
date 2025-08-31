from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        left = 0
        max_sequences = 0
        w = 0

        for right in range(1, len(nums)):
            if nums[right] <= nums[right - 1]:
                left = right
            elif nums[right] > nums[right - 1]:
                w = right - left + 1
            else:
                w = 0

            max_sequences = max(max_sequences, w)

        return max_sequences if max_sequences > 0 else 1


solution = Solution()
result = solution.findLengthOfLCIS([1, 3, 5, 4, 7])
print(result)
