from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        count = {n : 0 for n in nums}
        for n in nums:
            if count[n] <= 0:
                count[n] +=1
            else:
                return True

        return False

solution = Solution()
result = solution.hasDuplicate([1,2,3,3])
print(result)
        
