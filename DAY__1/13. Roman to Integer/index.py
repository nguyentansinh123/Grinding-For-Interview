
class Solution:
    def romanToInt(self, s: str) -> int:
        romanChar = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M":1000}
        romanCharArr = list(s)
        result = 0 
        for i in range(len(romanCharArr)):
            if i < len(romanCharArr) - 1 and romanChar[romanCharArr[i]] < romanChar[romanCharArr[i + 1]]:
                result -= romanChar[romanCharArr[i]]
            else:
                result += romanChar[romanCharArr[i]] 
        return result
    

solution = Solution()
result = solution.romanToInt('LVIII')
print(result)