from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[list[int]]:
        res = []
        sol = []
        n = len(nums)

        def backTrack(i):
            if i == n:
                res.append(sol[:])
                return

            backTrack(i + 1)

            sol.append(nums[i])
            backTrack(i + 1)
            sol.pop()

        backTrack(0)

        return res


solution = Solution()
result = solution.subsets([1, 2, 3])
