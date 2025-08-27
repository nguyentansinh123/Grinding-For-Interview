from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        setNums = sorted(nums)
        hash = {}
        res = []

        for i in range(len(setNums)):
            if setNums[i] not in hash:
                hash[setNums[i]] = i

        for e in nums:
            res.append(hash[e])

        return res


solution = Solution()
result = solution.smallerNumbersThanCurrent([8, 1, 2, 2, 3])
print(result)
