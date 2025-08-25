from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(crrStr):
            if len(crrStr) == n:
                res.append(crrStr[:])
                return

            for e in nums:
                if e not in crrStr:
                    crrStr.append(e)
                    backtrack(crrStr)
                    crrStr.pop()

        backtrack([])
        return res


solution = Solution()
result = solution.permute([1, 2, 3])
print(result)
