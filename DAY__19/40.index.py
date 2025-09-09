from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        def backtrack(i=0, arr=[], total=0):
            if total == target:
                output.append(arr)
                return
            if i >= len(candidates) or total > target:
                return
            backtrack(i + 1, arr + [candidates[i]], total + candidates[i])
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, arr, total)
        backtrack()
        return output

solution = Solution()
result = solution.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
print(result)
