class Solution:
    def isPalindrome(self, x: int) -> bool:
        stringNumber = list(str(x))
        newStr = ""
        for i in range(len(stringNumber)-1, -1 ,-1):
            newStr += stringNumber[i]            
        
        if newStr != str(x):
            return False
        else:
            return True


solution = Solution()
result = solution.isPalindrome(121)
print(result)