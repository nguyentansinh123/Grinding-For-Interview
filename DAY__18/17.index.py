from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtracking(i, currStr):
            if len(digits) == len(currStr):
                res.append(currStr)
                return
            
            for c in digitToChar[digits[i]]:
                backtracking(i + 1, currStr + c)

        if digits:
            backtracking(0,"")

        return res

solution = Solution()
result = solution.letterCombinations("23")
print(result)
