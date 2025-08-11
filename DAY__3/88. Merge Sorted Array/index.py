from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp = []
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                temp.append(nums1[p1])
                p1+=1
            else:
                temp.append(nums2[p2])
                p2+=1
        if p1 < m:
            temp.extend(nums1[p1:m])
        if p2 < n:
            temp.extend(nums2[p2:n])

        nums1[:m+n] = temp

solution = Solution()
result = solution.merge([1,2,3,0,0,0],3,[2,5,6],3)
print(result)