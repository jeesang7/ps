# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        # print(head)
        dummy_odd = odd = ListNode(0)
        dummy_even = even = ListNode(0)
        
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if even else None
            
        odd.next = dummy_even.next
        return dummy_odd.next
