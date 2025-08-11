class Solution:
    def isValid(self, s: str) -> bool:
        pattern = {"}":"{", "]":"[", ")":"("}
        stack = []


        for i in s:
            if i in pattern:
                if stack and stack[-1] == pattern[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False



solution = Solution()
result = solution.isValid("([])")
print(result)