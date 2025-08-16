from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0
        
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

solution = Solution()
my_nums = [2, 1]
solution.moveZeroes(my_nums) 
print(my_nums) 

my_nums_2 = [0, 1, 0, 3, 12]
solution.moveZeroes(my_nums_2)
print(my_nums_2) 


