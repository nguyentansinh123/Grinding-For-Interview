from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mySet = set()

        for i in nums:
            if i in mySet:
                mySet.remove(i)
            else:
                mySet.add(i)

        return mySet.pop()


solution = Solution()
result = solution.singleNumber([2, 2, 1])
print(result)
