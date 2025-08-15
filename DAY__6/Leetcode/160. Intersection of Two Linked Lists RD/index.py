from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        i = headA
        j = headB

        while i != j:
            i = i.next if i else headB
            j = j.next if j else headA       
        
        return i

        

solution = Solution()
result = solution.getIntersectionNode([1,9,1,2,4], [3,1,2,4])
print(result)