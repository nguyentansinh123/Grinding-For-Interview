from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = 0
        profit = []

        for sell in range(1,len(prices)):
            if prices[sell] - prices[buy] < 0:
                buy = sell
            profit.append(prices[sell] - prices[buy])
        
        return 0 if not profit else max(profit)

        
            

solution = Solution()
result = solution.maxProfit([7,1,5,3,6,4])
print(result)