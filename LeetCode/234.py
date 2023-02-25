# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        rev = []
        fast, slow = head, head
        while fast and fast.next:
            rev.append(slow.val)
            fast = fast.next.next
            slow = slow.next

        if fast:
            slow = slow.next
            
        while rev:
            if rev.pop() != slow.val:
                return False
            slow = slow.next

        return True