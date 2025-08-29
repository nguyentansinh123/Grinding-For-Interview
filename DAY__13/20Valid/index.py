class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "]": "[", "}": "{"}
        stack = []

        if len(s) <= 1:
            return False

        for i in s:
            if stack and i in brackets and brackets[i] == stack[-1]:
                print("yes")
                stack.pop()
            else:
                stack.append(i)
        return False if stack else True


solution = Solution()
print(solution.isValid("){"))
