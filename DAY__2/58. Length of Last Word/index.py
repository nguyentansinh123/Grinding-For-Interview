class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        newS = s.strip().split()
        return len(newS[-1])
solution = Solution()
result = solution.lengthOfLastWord("   fly me   to   the moon  ")
print(result)
