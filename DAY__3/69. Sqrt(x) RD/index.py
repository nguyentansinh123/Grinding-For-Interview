class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        arr = []
        for i in range(x + 1): 
            if i * i <= x:
                arr.append(i)
            if i * i > x:
                return arr[-1]
        return arr[-1]


solution = Solution()
result = solution.mySqrt(1)
print(result)