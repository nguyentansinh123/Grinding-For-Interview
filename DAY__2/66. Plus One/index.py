from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strsN = ""

        for i in digits:
            strsN += str(i)
        newList = str(int(strsN) + 1)
        arr = []
        for i in range(len(newList)):
            arr.append(int(newList[i]))

        return arr

solution = Solution()
result = solution.plusOne([1,2,3])
print(result)
