from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        row = [[1]]

        if numRows == 1:
            return row

        for _ in range(numRows - 1):

            temp = [0] + row[-1] + [0]
            arr = []

            for j in range(len(row[-1]) + 1):
                arr.append(temp[j] + temp[j +1])
            row.append(arr)
        
        return row



solution = Solution()
result = solution.generate(5)
print(result)