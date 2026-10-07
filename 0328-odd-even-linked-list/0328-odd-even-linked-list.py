# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next :
            return head
        current = head
        even = y = ListNode()
        odd = x = ListNode()
        cnt = 0
        while current :
            if cnt == 0 :
                x.next = current
                current = current.next
                x = x.next
                x.next = None
                cnt = 1
            else :
                y.next = current
                current = current.next
                y = y.next
                y.next = None
                cnt = 0
            # print(odd.next)
        
        x.next = even.next
        # print(x)
        return odd.next