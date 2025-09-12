from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {n:0 for n in nums}

        for n in nums:
            count[n] += 1

        sorted_items = sorted(count.items(), key=lambda x:x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]

solution = Solution()
result = solution.topKFrequent([1,2,2,3,3,3], 2)
print(result)
