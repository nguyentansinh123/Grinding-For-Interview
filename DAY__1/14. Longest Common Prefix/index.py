from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = ""

        for i in range(len(strs[0])):
            for j in strs:
                if i == len(j) or strs[0][i] != j[i]:
                    return commonPrefix
            commonPrefix +=strs[0][i]
        return commonPrefix

solution = Solution()   
result = solution.longestCommonPrefix(["flower","flow","flight"])
print(result)