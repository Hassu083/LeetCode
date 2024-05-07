# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy_d = dummy
        while head and head.next:
            dummy_d.next = head.next
            temp = head.next.next
            head.next = None
            dummy_d.next.next = head
            dummy_d = dummy_d.next.next
            head = temp
        dummy_d.next = head
        return dummy.next