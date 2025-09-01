from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_count = 10**9
        left = 0
        curr = 0

        for right in range(len(nums)):
            curr += nums[right]

            while curr >= target:
                min_count = min(min_count, right - left + 1)
                curr -= nums[left]
                left += 1

        return 0 if min_count == 10**9 else min_count


solution = Solution()
result = solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
print(result)
