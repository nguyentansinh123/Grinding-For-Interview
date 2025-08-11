from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0 

        for right in range(len(nums)):
            if nums[right] == val:
                continue
            else:
                nums[left] = nums[right]
                left +=1 
        return len(nums) - (len(nums) - left) 

solution = Solution()
result = solution.removeElement([0,1,2,2,3,0,4,2], 2)
print(result)