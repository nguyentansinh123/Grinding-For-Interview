from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        

        if len(nums) == 1:
            return nums[0]

        hash = {}

        for i in nums:
            if i not in hash:
                hash[i] = 1
            else:
                hash[i] +=1
        
        for key, value in hash.items():
            if value == 1:
                return key


solution = Solution()
result = solution.singleNumber([4,1,2,1,2])
print(result)