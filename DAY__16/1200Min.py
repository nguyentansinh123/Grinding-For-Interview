from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_dif = float("inf")
        arr.sort()
        res = []

        for i in range(1, len(arr)):
            curr = abs(arr[i] - arr[i - 1])

            if min_dif > curr:
                min_dif = curr
                res = [[arr[i - 1], arr[i]]]
            elif min_dif == curr:
                res.append([arr[i - 1], arr[i]])

        return res


solution = Solution()
result = solution.minimumAbsDifference([4, 2, 1, 3])
print(result)
