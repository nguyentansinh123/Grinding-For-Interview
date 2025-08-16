

class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
            (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
            (5, "V"), (4, "IV"), (1, "I")
        ]

        res = []

        for val, sym in symList:
            while num >= val:
                num -= val
                res.append(sym)
        
        return "".join(res)
                 
            



solution = Solution()
result = solution.intToRoman(3749)
print(result)