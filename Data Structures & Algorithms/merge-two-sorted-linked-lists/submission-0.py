# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        p = list1
        q = list2
        result = ListNode(-1)
        res= result
        
        while p and q:
            if p.val<q.val:
                tmp = ListNode(p.val)
                result.next = tmp
                result = tmp
                p=p.next
            elif p.val>q.val:
                tmp = ListNode(q.val)
                result.next = tmp
                result = tmp
                q=q.next
            else:
                tmp = ListNode(p.val)
                result.next = tmp
                result = tmp
                tmp = ListNode(q.val)
                result.next = tmp
                result = tmp
                q=q.next
                p=p.next
        while p:
            tmp = ListNode(p.val)
            result.next = tmp
            result = tmp
            p=p.next
        while q:
            tmp = ListNode(q.val)
            result.next = tmp
            result = tmp
            q=q.next
        return res.next