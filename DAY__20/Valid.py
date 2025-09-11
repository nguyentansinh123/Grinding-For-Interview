class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        

solution = Solution()
result = solution.isAnagram("racecar", "carrace")
print(result)
