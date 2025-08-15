from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head

        while pointer and pointer.next:

            if pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        
        return head


solution = Solution()
result = solution.deleteDuplicates([1,1,2])