from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        res = 0

        for right in range(1, len(prices)):
            if prices[right] < prices[left]:
                left = right
            else:
                profit = prices[right] - prices[left]
                res = max(res, profit)
        return res


solution = Solution()
result = solution.maxProfit([7, 1, 5, 3, 6, 4])
print(result)
