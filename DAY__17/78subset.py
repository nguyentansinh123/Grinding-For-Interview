from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            # add more number

            subset.append(nums[i])
            backtrack(i + 1)

            # dont add

            subset.pop()
            backtrack(i + 1)

        backtrack(0)

        return res


solution = Solution()
result = solution.subsets([1, 2, 3])
print(result)
