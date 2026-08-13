# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
[
    
    [1,2,4],

    [1,3,5],
    
    [3,6]

]

"""

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for i in range(len(lists)):
            curr =lists[i]
            while curr:
                arr.append(curr)
                curr = curr.next

        arr = sorted(arr,key=lambda x: x.val)
        if not len(arr):
            return None
        head = arr[0]
        curr = head
        print(curr)
        for node in range(1,len(arr)):
            curr.next = arr[node]
            curr = arr[node]

        return head
        
