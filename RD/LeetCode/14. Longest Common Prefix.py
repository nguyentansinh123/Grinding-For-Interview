from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        str = ""

        for i in range(len(strs[0])):

            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return str
            str += strs[0][i]
        return str

solution = Solution()
result = solution.longestCommonPrefix(["flower","flow","flight"])
print(result)