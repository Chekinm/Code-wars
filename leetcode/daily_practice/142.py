from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ids = set()
        
        while head and head.next:
            if id(head) in ids:
                return True
            ids.add(id(head))
            head = head.next

        return False