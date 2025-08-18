


class Solution:
    def longestPalindrome(self, s: str) -> str:
       
       longest_sub = ""

       if s == s[::-1]:
           return s
       for i in range(len(s)):
           
           for j in range(i, len(s)):
               
               substring = s[i:j+1]

               if substring == substring[::-1]:
                   if len(substring) > len(longest_sub):
                    longest_sub = substring
       return longest_sub
            
           

solution = Solution()
result = solution.longestPalindrome("babad")
print(result)