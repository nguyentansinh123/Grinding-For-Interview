from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        p = 1

        for s in range(1,len(nums)):

            if nums[s] != nums[s - 1]:
                nums[p] = nums[s]
                p+=1
        
        return p



solution = Solution()
result = solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(result)