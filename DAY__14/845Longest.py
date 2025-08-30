from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        longest = 0

        for p in range(1, len(arr) - 1):
            if arr[p] > arr[p + 1] and arr[p] > arr[p - 1]:
                left, right = p, p

                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1

                while right < len(arr) - 1 and arr[right] > arr[right + 1]:
                    right += 1

                longest = max(longest, right - left + 1)

        return longest


solution = Solution()
result = solution.longestMountain([2, 1, 4, 7, 3, 2, 5])
print(result)
