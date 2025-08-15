from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slower = head
        faster = head

        while faster and faster.next:

            faster = faster.next.next        
            slower = slower.next

            if  slower == faster:
                return True
        
        return False



solution = Solution()
result = solution.hasCycle([3,2,0,-4])
print(result)