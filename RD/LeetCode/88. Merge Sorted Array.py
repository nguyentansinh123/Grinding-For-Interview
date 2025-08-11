
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        i = 0 
        j = 0
        mergeArr = []

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                mergeArr.append(nums1[i])
                i += 1
            else:
                mergeArr.append(nums2[j])
                j+=1

        while i < m:
            mergeArr.append(nums1[i])
            i+=1
        while j < n:
            mergeArr.append(nums2[j])
            j+=1
        
        nums1[:] = mergeArr
solution = Solution()
result = solution.merge([1,2,3,0,0,0], 3, [2,5,6],3)
print(result)