from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backTrack(i, curSum, total):
            if total == target:
                res.append(curSum)
                return
            if total > target or i == len(candidates):
                return 
            
            backTrack(i, curSum + [candidates[i]], total + candidates[i])
            backTrack(i + 1, curSum, total)
        backTrack(0,[],0)

        return res



        
solution = Solution()
result = solution.combinationSum([2,3,6,7], 7)
print(result)
