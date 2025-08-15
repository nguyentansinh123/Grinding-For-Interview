from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        new_arr = nums1 + nums2
        sortArr = sorted(new_arr)

        if len(sortArr) <= 1:
            return sortArr[0]


        if len(sortArr) % 2 == 0:
            return (sortArr[len(sortArr) // 2] + sortArr[len(sortArr) // 2 - 1]) / 2
        
        else:
            return sortArr[len(sortArr) // 2]

solution = Solution()
result = solution.findMedianSortedArrays([1,2], [3,4])
print(result)