from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_len = 0

        for right in range(len(nums)):
            # If the current element is 0, we use one of our k flips.
            if nums[right] == 0:
                k -= 1

            # If k is negative, we have used more flips than allowed.
            # We must shrink the window from the left.
            while k < 0:
                # If the element at the left was a 0, we regain a flip.
                if nums[left] == 0:
                    k += 1
                # Shrink the window.
                left += 1
            
            max_len = max(max_len, right - left + 1)

        return max_len


solution = Solution()
result = solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2)
print(result)
