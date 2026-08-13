# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head
        if not head:
            return head

        while current:
            count+=1
            current=current.next

        current = head
        index_count = count-n
        prev = None
        count= 0
        while count<index_count:
            prev = current
            current = current.next
            count+=1

        if prev:
            prev.next = current.next
            return head
        else:

            return current.next