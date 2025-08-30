class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        mySet = set()
        longest = 0

        for right in range(len(s)):
            while s[right] in mySet:
                mySet.remove(s[left])
                left += 1

            mySet.add(s[right])
            longest = max(longest, right - left + 1)

        return longest


solution = Solution()
result = solution.lengthOfLongestSubstring("abcabcbb")
print(result)
