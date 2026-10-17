# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = dummy = ListNode(0,head)
        curr = head

        while curr :
            if curr.next and curr.next.val == curr.val :
                value = curr.val
                while curr and curr.val == value :
                    curr = curr.next
                prev.next = curr
            else :
                prev = curr
                curr = curr.next 

        return dummy.next