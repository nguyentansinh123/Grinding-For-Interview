from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        coins.sort(reverse=True)
        pointer = 0
        count = 0

        while pointer < len(coins):
            if amount >= coins[pointer]:
                count += 1
                amount -= coins[pointer]
            else:
                pointer += 1

        return count if amount == 0 else -1


solution = Solution()
result = solution.coinChange([1, 2, 5], 11)
print(result)
