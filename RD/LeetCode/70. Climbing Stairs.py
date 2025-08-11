


class Solution:
    def climbStairs(self, n: int) -> int:
       if n <= 1:
           return 1
       
       one, two = 1,2

       for _ in range(n - 2):
           temp = one + two
           one = two
           two = temp
       return two

solution = Solution()
result = solution.climbStairs(2)
print(result)