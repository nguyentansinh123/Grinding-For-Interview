from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left = 0
        seen = set()

        for right in range(len(nums)):
            if right - left > k:
                seen.remove(left)
                left += 1

            if nums[right] in seen:
                return True
            seen.add(nums[right])

        return False


solution = Solution()
result = solution.containsNearbyDuplicate([1, 2, 3, 1], 3)
print(result)
