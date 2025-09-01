class Solution:
    def climbStairs(self, n: int) -> int:
        two, one = 1, 1

        for i in range(n - 1):
            temp = two
            two = one + two
            one = temp
        return two


solution = Solution()
result = solution.climbStairs(5)
print(result)
