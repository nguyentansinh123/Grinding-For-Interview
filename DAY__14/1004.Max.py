from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        num_zero = 0
        left = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                num_zero += 1

            while num_zero > k:
                if nums[left] == 0:
                    num_zero -= 1
                left += 1

            w = right - left + 1
            max_len = max(max_len, w)

        return max_len


solution = Solution()
result = solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
print(result)
