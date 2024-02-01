
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        heads_k = []
        i = 0
        while head:
            if i % k == 0:
                heads_k.append(head)
            head = head.next
            i += 1

        if i % k != 0:  # check lenght, if non devisibal by k
            ans = heads_k[-1]
            heads_k.pop()
        else:            # devisibal, reverse all
            ans = None

        # revert chunks
        while heads_k:
            to_rev = heads_k[-1]
            count = 0
            while to_rev and count < k:
                ans = ListNode(to_rev.val, ans)
                to_rev = to_rev.next
                count += 1
            heads_k.pop()

        return ans
