
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        count = 0
        current = head

        while current:
            count+=1
            current=current.next


        def reverse(h):
            current = h
            prev = None

            while current!=None:
                tmp = current.next
                current.next = prev
                prev = current
                current = tmp

            return prev

        current_count = 0
        mid = count//2
        if count%2==0:
            mid-=1
        current = head


        while current_count<mid:
            current= current.next
            current_count+=1

        mid_node = reverse(current.next)
        current.next = None
        
        current = head

        while mid_node:
            tmp_current = current.next
            tmp_mid = mid_node.next

            current.next = mid_node
            if tmp_current:
                mid_node.next = tmp_current


            current = tmp_current
            mid_node = tmp_mid
        return None
