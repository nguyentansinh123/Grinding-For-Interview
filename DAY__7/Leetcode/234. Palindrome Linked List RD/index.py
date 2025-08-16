from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        curr = head

        res = []

        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return res == res[::-1]

        


solution = Solution()
result = solution.isPalindrome([1,2,2,1])
print(result)