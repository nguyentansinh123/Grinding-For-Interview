from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       hashMap = {}
       for index, number in enumerate(nums):
            numberToFind = target - number        
            if numberToFind in hashMap:
                return [hashMap[numberToFind] , index]
            else:
                hashMap[number] = index

solution = Solution()
result = solution.twoSum([2,7,11,15],9)
print(result)