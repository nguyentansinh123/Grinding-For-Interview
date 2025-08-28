from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time = 0
        x1, y1 = points.pop()

        while points:
            x2, y2 = points.pop()
            total_time += max(abs(x2 - x1), abs(y2 - y1))

            x1, y1 = x2, y2

        return total_time


solution = Solution()
result = solution.minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]])
print(result)
