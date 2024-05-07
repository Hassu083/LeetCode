# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def double(head):
            if not head:
                return 0
            carry = double(head.next) 
            value = head.val*2 + carry
            head.val = value%10
            return value//10
        carry = double(head) 
        while carry:
            head = ListNode(carry%10, head) 
            carry //= 10
        return head